#!/usr/bin/env python
#coding=utf-8

"""
Copyright (c) 2014 secfree, released under the GPL license

Author: secfree
Email: zzd7zzd#gmail.com
"""

import sys
import getopt
import logging
import sqlite3
import threading
import socket
import hashlib
import StringIO
import urlparse
import time

import pycurl


COOKIE = ''
DIR_PROBE_EXTS = ['.tar.gz', '.zip', '.rar', '.tar.bz2']
FILE_PROBE_EXTS = ['.bak', '.swp', '.1']
NOT_EXIST = hashlib.md5("not_exist").hexdigest()[8:16]


def usage():
    print """
    Usage:
        bcrpscan.py (-i import_url_list_file | -u url) [-c cookie_file] [-d db_path] [-h]
    """


def probe_url(url):
    """
    Scan web path based on an url.

    :param url: url
    :type url: str
    """
    if not url or not url.startswith('http'):
        return
    if url.count('/') == 2:
        url = '%s/' % url
    if url[-1] != '/':
        code, rurl, length = get_url(url)
        durl = '%s/' % url
        if code/100 == 3 and rurl and rurl.startswith(durl):
            url = durl

    pr = urlparse.urlparse(url)
    paths = get_parent_paths(pr.path)
    for p in paths:
        if p[-1] == '/':
            for ext in DIR_PROBE_EXTS:
                u = '%s://%s%s%s' % (pr.scheme, pr.netloc, p[:-1], ext)
                code, rurl, length = get_url(u)
                if code == 200:
                    logging.info("[+] %s" % u)
        else:
            for ext in FILE_PROBE_EXTS:
                u = '%s://%s%s%s' % (pr.scheme, pr.netloc, p, ext)
                code, rurl, length = get_url(u)
                if code == 200:
                    logging.info("[+] %s" % u)


def get_parent_paths(path):
    '''
    Get a path's parent paths.

    :param path: path
    :type path: str
    
    :rparam: parent paths
    :rtype: list
    '''
    paths = []
    if not path or path[0] != '/':
        return paths
    paths.append(path)
    tph = path
    if path[-1] == '/':
        tph = path[:-1]
    while tph:
        tph = tph[:tph.rfind('/')+1]
        paths.append(tph)
        tph = tph[:-1]
    return paths


def get_url(url):
    '''
    Request a url.

    :param url: url
    :type url: str

    :rparams: (code, rurl, length)
    :rtypes: (int, str, int)
    '''
    logging.info(url)

    # set pycurl request
    pcr = pycurl.Curl()
    pcr.setopt(pycurl.FOLLOWLOCATION, 0)
    pcr.fp = StringIO.StringIO()
    pcr.setopt(pcr.WRITEFUNCTION, pcr.fp.write)
    pcr.setopt(pycurl.TIMEOUT, 10)
    pcr.setopt(pycurl.NOSIGNAL, 1)
    try:
        pcr.setopt(pycurl.URL, str(url))
    except TypeError as err:
        logging.info('type: %s -- err: %s' % (str(type(url)), str(err)))
        return (0, '', 0)

    # set cookie
    if COOKIE:
        pcr.setopt(pycurl.COOKIE, COOKIE)

    # request url
    try:
        pcr.perform()
    except pycurl.error as err:
        logging.error('url: %s -- %s' % ( url, str(err)))
        if 'transfer closed' not in str(err):
            return (0, '', 0)

    code = pcr.getinfo(pycurl.HTTP_CODE)
    rurl = pcr.getinfo(pycurl.REDIRECT_URL)
    html = pcr.fp.getvalue()
    length = len(html)

    # response is null
    if (code == 200) and (length == 1) and (ord(html[0]) == 0):
        return (0, '', 0)
    if (length < 2049) and ('document.location= "http://sh.114so.cn/"' in html):
        return (0, '', 0)

    pcr.close()
    return (code, rurl, length)


def set_log():
    '''
    set log
    '''
    format = "%(asctime)s  %(levelname)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO)


class Db_path:
    '''
    sqlite db operation
    '''
    def __init__(self):
        self.con = None
        self.cur = None
       
    def connect(self, db_file):
        '''
        connect to db_file
        '''
        self.con = sqlite3.connect(db_file)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
   
    def create(self):
        '''
        create table
        '''
        sql_create = [
        '''
        create table if not exists webpath (
        id integer primary key autoincrement,
        host varchar(1024),
        scheme varchar(10),
        path varchar(1024),
        probed integer
        );
        ''',
        '''
        create table if not exists vuln (
        id integer primary key autoincrement,
        url varchar(1024),
        code varchar(10),
        length integer
        )
        '''
        ]
        try:
            for sql in sql_create:
                self.cur.execute(sql)
            self.con.commit()
        except sqlite3.Error as err:
            logging.error('%s:%s %s',  __file__, sys._getframe().f_lineno, str(err))
            return False
        return True
   
    def insert(self, table, st):
        '''
        do insert
        '''
        keys = {}
        keys['webpath'] = ('host', 'scheme', 'path', 'probed')
        keys['vuln'] = ('url', 'code', 'length')
        values = []
        ikys = ''
        n = len(keys[table])
        for i in range(n):
            ikys += '%s, ' % keys[table][i]
            values.append(st[keys[table][i]])
        ikys = ikys[:-2]
        iqs = '?, ' * n
        iqs = iqs[:-2]
        sql = 'insert into %s(%s) values(%s);' % (table, ikys, iqs)
        try:
            self.cur.execute(sql, values)
        except sqlite3.Error as err:
            logging.error('%s:%s %s',  __file__, sys._getframe().f_lineno, str(err))
            return False
        return True
       
    def commit(self):
        try:
            self.con.commit()
        except sqlite3.Error as err:
            logging.error('%s:%s %s',  __file__, sys._getframe().f_lineno, str(err))
            return False
        return True
   
    def update(self, table, conditions=None, **kwargs):
        '''
        update table
        '''
        if len(kwargs) == 0:
            return True
        values = []
        sql = 'update %s set ' % table
        for k in kwargs:
            sql += '%s = ?, ' % k
            values.append(kwargs[k])
        sql = sql[:-2]
        if conditions and len(conditions) > 0:
            sql += ' where'
            for k in conditions:
                sql += ' %s=? and ' % k
                values.append(conditions[k])
            sql = sql[:-5]
        sql += ';'
       
        try:
            self.cur.execute(sql, values)
        except sqlite3.Error as err:
            logging.error('%s:%s %s',  __file__, sys._getframe().f_lineno, str(err))
            return False
        return True
   
    def fetch(self, table, num = None, keys=(), **conditions):
        '''
        fetch rows from table
        '''
        values = []
        sql = 'select '
        if len(keys) > 0:
            for k in keys:
                sql += '%s, ' % k
            sql = sql[:-2]
        else:
            sql += '*'
        sql += ' from %s ' % table
        if len(conditions) > 0:
            sql += 'where'
            for k in conditions:
                sql += ' %s=? and ' % k
                values.append(conditions[k])
            sql = sql[:-5]
        if num:
            sql += ' limit ?'
            values.append(num)
        sql += ';'
       
        try:
            self.cur.execute(sql, values)
            rows = self.cur.fetchall()
        except sqlite3.Error as err:
            logging.error('%s:%s %s',  __file__, sys._getframe().f_lineno, str(err))
            return None
       
        return rows
   
    def query(self, sql):
        '''
        execute a query sql
        '''
        try:
            self.cur.execute(sql)
            rows = self.cur.fetchall()
        except sqlite3.Error as err:
            logging.error('%s:%s %s',  __file__, sys._getframe().f_lineno, str(err))
            return None
       
        return rows
       
    def close(self):
        self.cur.close()
        self.con.close()
        

def add_path(db, pr):
    """
    Add url to database.

    :param db: database
    :type db: object

    :param pr: url parse result
    :type pr: object
    """
    paths = get_parent_paths(pr.path)
    for p in paths:
        rows = db.fetch(
            'webpath',
            host = pr.netloc,
            scheme = pr.scheme,
            path = p
            )
        if not rows:
            st = {}
            st['host'] = pr.netloc
            st['scheme'] = pr.scheme
            st['path'] = p 
            st['probed'] = 0
            db.insert('webpath', st)
    db.commit()


def th_get_real_url(url, 
    real_urls, 
    bsm, 
    lock
    ):
    """
    A thread judge whether the url's path is directory and add it to real_urls.

    :param url: url
    :type url: str

    :param real_urls: list of real urls
    :type real_urls: list

    :param bsm: BoundedSemaphore object
    :type bsm: object

    :param lock: Lock object
    :type lock: object
    """
    code, rurl, length = get_url(url)
    durl = '%s/' % url
    if code == 200:
        lock.acquire()
        real_urls.append(url)
        lock.release()
    elif code/100 == 3 and rurl and rurl.startswith(durl):
        lock.acquire()
        real_urls.append(durl)
        lock.release()
    bsm.release()


def import_file(path, db):
    """
    Imort urls from a file.

    :param path: path of url file
    :type path: str

    :param db: database
    :type db: object
    """
    bsm = threading.BoundedSemaphore(30)
    lock = threading.Lock()
    real_urls = []
    ths = []

    fs = open(path)
    for line in fs:
        line = line.strip()
        if not line.startswith('http'):
            continue
        if line.count('/') == 2:
            line = '%s/' % line
        
        pr = urlparse.urlparse(line)
        rows = db.fetch(
            'webpath',
            host = pr.netloc,
            scheme = pr.scheme,
            path = pr.path
             )
        if rows:
            continue
        if line[-1] != '/':
            rows = db.fetch(
            'webpath',
            host = pr.netloc,
            scheme = pr.scheme,
            path = '%s/' % pr.path
             )
            if rows:
                continue
            bsm.acquire()
            th = threading.Thread(
                target=th_get_real_url,
                args=(line, real_urls, bsm, lock)
                )
            # The main thread exit, the son should thread exit too.
            # Sometimes get_url() may be stocked.
            th.setDaemon(True)
            th.start()
            ths.append(th)
        else:
            add_path(db, pr)

    # wait until socket timeout
    time.sleep(10)
    for th in ths:
        th.join()
    fs.close()

    for u in real_urls:
        pr = urlparse.urlparse(u)
        add_path(db, pr)
    real_urls = []


def th_probe_url(
    url, 
    vulns,
    bsm,
    lock
    ):
    """
    A thread probe a url.

    :param url: url
    :type url: str

    :param vulns: vulns list
    :type vulns: list

    :param bsm: BoundedSemaphore object
    :type bsm: object

    :param lock: Lock object
    :type lock: object
    """
    global COOKIE, DIR_PROBE_EXTS, FILE_PROBE_EXTS, NOT_EXIST

    tmp_vus = []
    if url[-1] == '/':
        u = '%s%s' % (url[:-1], NOT_EXIST)
        code, rurl, length = get_url(u)
        if code != 200:
            for ext in DIR_PROBE_EXTS:
                u = '%s%s' % (url[:-1], ext)
                code, rurl, length = get_url(u)
                if code == 200:
                    tmp_vus.append({'url': u, 'code': code, 'length': length})
    else:
        u = '%s%s' % (url, NOT_EXIST)
        code, rurl, length = get_url(u)
        if code != 200:
            for ext in FILE_PROBE_EXTS:
                u = '%s%s' % (url, ext)
                code, rurl, length = get_url(u)
                if code == 200:
                    tmp_vus.append({'url': u, 'code': code, 'length': length})

    # Sometimes, when getting NOT_EXIST url, its code is not 200 for network reasons.
    # At this time, vuln is not exist.
    if len(tmp_vus) == 1:
        lock.acquire()
        vulns.append(tmp_vus[0])
        lock.release()
        logging.info('[+] %s' % tmp_vus[0]['url'])

    bsm.release()
    

def probe(db):
    """
    Probe web path.

    :param db: database
    :type db: object
    """
    lock = threading.Lock()
    bsm = threading.BoundedSemaphore(30)
    vulns = []
    ths = []

    while True:
        rows = db.fetch('webpath', 1, probed = 0)
        if not rows or rows[0]['id'] == None:
            break
        st = rows[0]
        u = '%s://%s%s' % (st['scheme'], st['host'], st['path'])

        bsm.acquire()
        th = threading.Thread(
            target=th_probe_url,
            args=(u, vulns, bsm, lock)
            )
        # The main thread exit, the son should thread exit too.
        # Sometimes get_url() may be stocked.
        th.setDaemon(True)
        th.start()
        ths.append(th)

        db.update(
            'webpath', 
            conditions = {'id': st['id']},
            probed = 1,
            )
        db.commit()

    time.sleep(10)
    for th in ths:
        th.join()

    # put vulns into database
    check_ext = '250'
    for vn in vulns:
        # check url once more
        code, rurl, length = get_url('%s%s' % (vn['url'], check_ext))
        if code != 200:
            db.insert('vuln', vn)
    db.commit()


def show_vuln(db):
    """
    Display vulns in database.

    :param db: database
    :type db: object
    """
    rows = db.query("select url from vuln order by url;")
    if rows:
        print ''
        print '-' * 30
        print 'Probed web paths:'
        for r in rows:
            print r['url']


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
        sys.exit(-1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "c:d:hi:u:")
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(-1)

    url = ''
    url_file = ''
    db_path = './db'
    for t, a in opts:
        if t == '-c':
            with open(a) as f:
                COOKIE = f.read().strip()
        if t == '-d':
            db_path = a
        if t == '-h':
            usage()
            sys.exit(0)
        if t == '-i':
            url_file = a
        if t == '-u':
            url = ''

    if not url and not  url_file:
        usage()
        sys.exit(-1)

    socket.setdefaulttimeout(10.0)

    if url:
        probe_url(url)

    if url_file:
        set_log()

        db = Db_path()
        db.connect(db_path)
        db.create()

        import_file(url_file, db)

        probe(db)

        show_vuln(db)

        db.close()
