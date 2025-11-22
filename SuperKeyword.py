# class Parent_Class:
#     def parent_method(self):
#         print("This is the parent class..")

# class Child_Class(Parent_Class):
#     def child_method(self):
#         print("This is the child class....")
#         super().parent_method()
# c=Child_Class()
# c.child_method()

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        

Rohan=Programmer("rohan",2,"python")
print(Rohan.name)
print(Rohan.id)
print(Rohan.lang)
        