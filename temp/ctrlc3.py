#!/usr/bin/env python
import multiprocessing, os, time

def do_work(i):
	try:
		while True:
			print 'Work Started: %d %d' % (os.getpid(), i)
			time.sleep(2)
		return 'Success'
	except KeyboardInterrupt, e:
		pass

def main():
	pool = multiprocessing.Pool(3)
	p = pool.map_async(do_work, range(6))
	try:
		results = p.get(0xFFFF)
	except KeyboardInterrupt:
		print 'parent received control-c'
		return

	for i in results:
		print i

if __name__ == "__main__":
	main()