#dir method is used for getting informations on all methods that can be used for an object.
#dict methods is used to return values in dictionary form.
#help method is used to give all information of an object.

x=[1,2,3,4,5]
print(dir(x))

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("ram",12)
print(p1.__dict__)
print(help(p1))
