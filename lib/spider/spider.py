# coding:utf-8
import gevent
from gevent import (monkey,
                    queue,
                    event,
                    pool)

import re
import sys
import logging
import unittest
import urllib
import urlparse
import requests
from threading import Timer
from pyquery import PyQuery
from utils import HtmlAnalyzer, UrlFilter


__all__ = ['Strategy', 'UrlObj', 'Spider', 'HtmlAnalyzer', 'UrlFilter']



class Strategy(object):

    default_cookies = {}

    default_headers = {
        'User-Agent': 'SinaSec Webscan Spider',
        'Accept': 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    }


    def __init__(self,max_depth=5,max_count=5000,concurrency=5,timeout=10,time=6*3600,headers=None,
                 cookies=None,ssl_verify=False,same_host=False,same_domain=True):
        self.max_depth = max_depth
        self.max_count = max_count
        self.concurrency = concurrency
        self.timeout = timeout
        self.time = time
        self.headers = self.default_headers
        self.headers.update(headers or {})
        self.cookies = self.default_cookies
        self.cookies.update(cookies or {})
        self.ssl_verify = ssl_verify
        self.same_host = same_host
        self.same_domain = same_domain


class UrlObj(object):

    def __init__(self, url, depth=0, linkin=None):
        if not url.startswith("http"):
            url = "http://" + url
        self.url = url.strip('/')
        self.depth = depth
        self.linkin = linkin

    def __str__(self):
        return self.url

    def __repr__(self):
        return "<Url object: %s>" % self.url

    def __hash__(self):
        return hash(self.url)

    def setLinkin(self, urlobj):
        self.linkin = urlobj

    def incrDepth(self):
        self.depth += 1


class UrlTable(object):

    infinite = float("inf")

    def __init__(self, size=0):
        self.__urls = {}

        if size == 0 :
            size = self.infinite
        self.size = size

    def __len__(self):
        return len(self.__urls)

    def __contains__(self, url):
        return hash(url) in self.__urls.keys()

    def __iter__(self):
        for url in self.urls:
            yield url

    def insert(self, url):
        if isinstance(url, basestring):
            url = UrlObj(url)
        if url not in self:
            self.__urls.setdefault(hash(url), url)

    @property
    def urls(self):
        return self.__urls.values()

    def full(self):
        return len(self) >= self.size


class Spider(object):

    logger = logging.getLogger("spider.mainthread")

    def __init__(self,strategy=Strategy()):
        monkey.patch_all()
        self.strategy = strategy
        self.queue = queue.Queue()
        self.urltable = UrlTable(strategy.max_count)
        self.pool = pool.Pool(strategy.concurrency)
        self.greenlet_finished = event.Event()
        self._stop = event.Event()


    def setRootUrl(self,url):
        if isinstance(url,basestring):
            url = UrlObj(url)
        self.root = url
        self.put(self.root)

    def put(self, url):
        if url not in self.urltable:
            self.queue.put(url)

    def run(self):
        self.timer = Timer(self.strategy.time, self.stop)
        self.timer.start()
        self.logger.info("spider '%s' begin running",self.root)

        while not self.stopped() and self.timer.isAlive():
            for greenlet in list(self.pool):
                if greenlet.dead:
                    self.pool.discard(greenlet)
            try:
                url = self.queue.get_nowait()
            except queue.Empty:
                if self.pool.free_count() != self.pool.size:
                    self.greenlet_finished.wait()
                    self.greenlet_finished.clear()
                    continue
                else:
                    self.stop()
            greenlet = Handler(url, self)
            self.pool.start(greenlet)

    def stopped(self):
        return self._stop.is_set()

    def stop(self):
        self.logger.info("spider '%s' finished. fetch total (%d) urls",self.root,len(self.urltable))
        self.timer.cancel()
        self._stop.set()
        self.pool.join()
        self.queue.put(StopIteration)
        return

    def dump(self):
        import StringIO
        out = StringIO.StringIO()
        for url in self.urltable:
            try:
                print >> out ,url
            except:
                continue
        return out.getvalue()


class Handler(gevent.Greenlet):

    logger = logging.getLogger("spider.handler")

    def __init__(self, urlobj, spider):
        gevent.Greenlet.__init__(self)
        self.urlobj = urlobj
        self.spider = spider
        self.charset = "utf-8"

    def _run(self):
        strategy = self.spider.strategy
        urltable = self.spider.urltable
        queue = self.spider.queue

        try:
            html = self.open(self.urlobj.url)
        except Exception, why:
            self.logger.debug("open '%s' failed,since : %s", self.urlobj, why)
            return self.stop()

        linkin = self.urlobj
        depth = linkin.depth + 1

        if strategy.max_depth and (depth > strategy.max_depth):
            return self.stop()

        for link in self.feed(html):

            if urltable.full():
                self.stop()
                self.spider.stop()
                return

            if link in urltable:
                continue


            if strategy.same_host and (not UrlFilter.isSameHost(link,linkin.url)):
                continue

            if strategy.same_domain and (not UrlFilter.isSameDomain(link, linkin.url)):
                continue

            url = UrlObj(link, depth, linkin)
            urltable.insert(url)
            queue.put(url)

            self.logger.debug(
                "sucess crawled '%s' the <%d> urls", url, len(urltable))

        self.stop()

    def open(self, url):
        strategy = self.spider.strategy
        try:
            resp = requests.get(url, headers=strategy.headers,
                                cookies=strategy.cookies, timeout=strategy.timeout,
                                verify=strategy.ssl_verify)
        except requests.exceptions.RequestException, e:
            raise e
        if resp.status_code != requests.codes.ok:
            resp.raise_for_status()
        charset = HtmlAnalyzer.detectCharSet(resp.text)
        if charset is not None:
            self.charset = charset
            resp.encoding = charset
        return resp.text

    def feed(self,html):
        return HtmlAnalyzer.extractLinks(html,self.urlobj.url,self.charset)


    def stop(self):
        self.spider.greenlet_finished.set()
        self.kill(block=False)


class TestSpider(unittest.TestCase):

    def setUp(self):
        self.root = "http://www.sina.com.cn"
        strategy = Strategy(max_depth=3, max_count=5000,
                            same_host=False, same_domain=True)
        self.spider = Spider(strategy)
        self.spider.setRootUrl(self.root)
        self.spider.run()

    def testSpiderStrategy(self):
        self.assertEqual(len(self.spider.urltable), 5000)
        self.assertLessEqual(self.spider.urltable.urls[-1].depth, 3)
        for url in self.spider.urltable.urls[100:200]:
            self.assert_(UrlFilter.isSameDomain(self.root, str(url)))



if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG if "-v" in sys.argv else logging.WARN,
        format='%(asctime)s %(levelname)s %(message)s')
    unittest.main()
