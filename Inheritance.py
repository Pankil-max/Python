class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"Name={self.name} and Id={self.id}")


class Teacher(Employee):
    def language(self):
        print("The prioritized language is English")
e1=Teacher("Ram",12)
e1.showDetails()
e1.language()
e2=Employee("Shyam",13)
e2.showDetails()
        