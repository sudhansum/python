from threading import *
import time

i = 0
lk = Lock()


def inc():
    global i
    lk.acquire()
    for j in range(1, 6):
        i += 1
        time.sleep(1)
        print("after increment i =", i)
    lk.release()


def dec():
    global i
    lk.acquire() #acquire the lock
    for j in range(1, 6):
        i -= 1
        time.sleep(1)
        print("after decrement i =", i)
    lk.release() #release the lock


t1 = Thread(target=inc)
t2 = Thread(target=dec)
t1.start()
t2.start()
t1.join()
t2.join()
''' context switching is switching the process to another process
 will be swapped out and the 2nd process data will be processed
 '''
''' Thread based multitasking - Thread is a light weight process
memory management takes less time as they use the same address
'''
'''if multiple threads are waiting then thread scheduler decides which 
thread runs decided by the PVM'''
'''How sync works with locks'''
'''Every object in python has a built in lock and comes to play when 
the object has synchronized method code.Acquiring a lock for an object is 
 also known as locking the object'''
'''what is multiprocessing and what is multi threading?'''
