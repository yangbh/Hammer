#!/usr/bin/python2.7
#coding:utf-8
import multiprocessing, os, signal, time, Queue

def do_work():
	
	while True:
		print 'Work Started: %d' % os.getpid()
		time.sleep(2)
	return 'Success'

def manual_function(job_queue, result_queue):
	signal.signal(signal.SIGINT, signal.SIG_IGN)
	while not job_queue.empty():
		try:
			job = job_queue.get(block=False)
			result_queue.put(do_work())
		except Queue.Empty:
			pass
		#except KeyboardInterrupt: pass

def main():
	job_queue = multiprocessing.Queue()
	result_queue = multiprocessing.Queue()

	for i in range(6):
		job_queue.put(None)

	workers = []
	for i in range(3):
		tmp = multiprocessing.Process(target=manual_function,
									  args=(job_queue, result_queue))
		tmp.start()
		workers.append(tmp)

	try:
		for worker in workers:
			worker.join()
	except KeyboardInterrupt:
		print 'parent received ctrl-c'
		for worker in workers:
			worker.terminate()
			worker.join()

	while not result_queue.empty():
		print result_queue.get(block=False)

if __name__ == "__main__":
	main()