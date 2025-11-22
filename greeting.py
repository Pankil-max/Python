import time
timer=int(time.strftime("%H"))
showtime=time.strftime("%H:%M:%S")
print(showtime)
if(0 <= timer < 12):
    print("Good morning sir")
elif(12 <= timer < 18):
    print("good evening sir")
elif(18 <= timer < 22):
    print("Good night sir")
