import time
from threading import *


def func():
    for i in range(1, 6):
        print("I am a child thread",current_thread().name)
        time.sleep(1)


t2 = Thread(target=func)
t3=Thread(target=func)
#t2.name("Sudhansu")
#t3.name("Travel")
t2.start()
t3.start()
for i in range(1, 6):
    print('I am the main thread')
