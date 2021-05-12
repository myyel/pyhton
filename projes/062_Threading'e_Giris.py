
import threading
import time


def merhaba():
    for x in range(10):
        print("merhaba")
        time.sleep(0.3)

def naber():
    for x in range(10):
        print("naber")  
        time.sleep(0.5)


t1=threading.Thread(target=merhaba)
t2=threading.Thread(target=naber)

t1.start()
t2.start()
