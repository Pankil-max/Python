import time
# print(time.time())
t=time.localtime()
f_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(f_time)