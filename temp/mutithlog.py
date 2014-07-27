#!/usr/bin/python2.7
#coding:utf-8

import logging, logging.handlers, thread, threading, random

logging.raiseExceptions = 1

NUM_THREADS = 5
LOOP_COUNT = 10

LOG_MESSAGES = [
    (logging.DEBUG, "%3d This is a %s message", "debug"),
    (logging.INFO, "%3d This is an %s message", "informational"),
    (logging.WARNING, "%3d This is a %s message", "warning"),
    (logging.ERROR, "%3d This is an %s message", "error"),
    (logging.CRITICAL, "%3d This is a %s message", "critical"),
]

LOG_NAMES = ["A", "A.B", "A.B.C", "A.B.C.D"]

def doLog(num):
    logger = logging.getLogger('test')
    f = logging.Formatter("%(asctime)s %(levelname)-9s %(name)-8s %(thread)5s %(message)s")
    h = logging.FileHandler(str(num), 'w')
    h.setFormatter(f)
    logger.addHandler(h)
    logger.info("*** thread %s started (%d)", thread.get_ident(), num)

def test():
    f = logging.Formatter("%(asctime)s %(levelname)-9s %(name)-8s %(thread)5s %(message)s")
    root = logging.getLogger('')
    root.setLevel(logging.DEBUG)
    h = logging.FileHandler('thread.log', 'w')
    root.addHandler(h)
    h.setFormatter(f)
    h = logging.handlers.SocketHandler('localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT)
    #h = logging.handlers.DatagramHandler('localhost', logging.handlers.DEFAULT_UDP_LOGGING_PORT)
    root.addHandler(h)
    threads = []
    for i in xrange(NUM_THREADS):
        threads.append(threading.Thread(target=doLog, args=(len(threads),)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    test()
