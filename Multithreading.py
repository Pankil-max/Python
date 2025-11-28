import time
import threading
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

func(4)
func(3)
func(2)
func(1)



t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[2])
t4=threading.Thread(target=func,args=[1])
# t1.join .join goes to next threadings only if first completed

