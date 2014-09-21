import time
import random
import threading
bigLock = threading.Lock()
a = 0
def Audit():
	global a,bigLock
	bigLock.acquire()
	a = a+1
	tt = random.randint(0, 10)
	time.sleep(tt)
	retinfo = a
	a =0
	bigLock.release()
	return retinfo