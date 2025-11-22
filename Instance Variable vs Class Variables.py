class Employee:
    CompanyName="Apple"
    NoofEmp=0

    def __init__(self,name):
        self.name=name
        self.raise_amt=0.02
        Employee.NoofEmp+=1
    def info(self):
        print(f"Name={self.name}, Raise in salary={self.raise_amt} and CompanyName={self.CompanyName} where total no of emp={self.NoofEmp}")

e1=Employee("Rohan")
e1.CompanyName="Apple India"
e1.info()
Employee.CompanyName="ORACLE"
e2=Employee("Rahul")
e2.info()

