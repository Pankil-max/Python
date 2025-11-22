# (a=3,b=3) Tis is default value if none of the value is assigned
# def average(a=3,b=3):
#     print("Average=",(a+b)/2)
# average(6,7)

def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=avg(1,2,3,4)
print(c)
 