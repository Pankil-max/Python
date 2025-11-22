class Employee:
    CompanyName="Apple"

    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Name={self.name} and CompanyName={self.CompanyName}")
    @classmethod
    def change(cls,company):
        cls.CompanyName=company


e1=Employee("Pankil")
e1.change("tesla")
e1.show()
print(Employee.CompanyName)