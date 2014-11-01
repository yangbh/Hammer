#!/usr/bin/env python
import multiprocessing, os, time

def do_work():
	while True:
		print 'Work Started: %d' % os.getpid()
		time.sleep(2)
	return 'Success'

def pool_function():
	try:
		return do_work()
	except KeyboardInterrupt:
		return 'KeyboardException'

def main():
	pool = multiprocessing.Pool(3)
	try:
		jobs = []
		for i in range(6):
			jobs.append(pool.apply_async(pool_function, args=()))
		pool.close()
		pool.join()
	except KeyboardInterrupt:
		print 'parent received control-c'
		pool.terminate()

	for i in jobs:
		if i.successful():
			print i.get()
		else:
			print 'Job failed: %s %s' % (type(i._value), i._value)

if __name__ == "__main__":
	main()