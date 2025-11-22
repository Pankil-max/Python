#MAP
def cube(x):
    return x*x*x

l=[1,2,3,4,5,6,7]
l1=list(map(cube,l))
print(l1) 

#FLITER
l2=list(filter(lambda x:x>4,l))
print(l2)

#REDUCE
from functools import reduce
l3=reduce(lambda x,y:(x-y),l)
print(l3)
