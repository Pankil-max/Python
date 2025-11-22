class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls,string):
    
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1=Employee("Ram",1200)
print(e1.name,e1.salary)
e2=Employee.fromstr(("harry-40000000000"))
print(e2.name,e2.salary)
