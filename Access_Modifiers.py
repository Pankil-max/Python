# There is no concept such as private,protected and public in python but can be used as a convention
# Public(Convention)
class Employee:
    def __init__(self,name):
        self.name="pankil"

e1=Employee("Ram")
print(e1.name)

#Private(Convention)__after self. makes private but can be accessed by _ClassName__name
class Student:
    def __init__(self,name):
        self.__name=name

e1=Student("Ram")
print(e1._Student__name)
