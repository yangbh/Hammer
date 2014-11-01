import multiprocessing
import time
import signal
import sys

'''
经测试，未执行到pool.join()内时，可以截获KeyboardInterrupt异常，再调用pool.terminate()结束子进程
但是当已经执行到pool.join()内时，ctrl＋c是不能断的
'''

def init_worker():
	signal.signal(signal.SIGINT, signal.SIG_IGN)

def worker():
	while(True):
		time.sleep(1.1234)
		print "Working..."

if __name__ == "__main__":
	pool = multiprocessing.Pool(8, init_worker)
	try:
		for i in range(8):
			pool.apply_async(worker)

		time.sleep(2)
		pool.close()
		pool.join()

	except KeyboardInterrupt:
		print "Caught KeyboardInterrupt, terminating workers"
		pool.terminate()
		# pool.join()
		pass