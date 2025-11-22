# Used to create objects
class Person:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
        print("Hello I am a person")
    

  
    def info(self):
        print(f"{self.name} is a {self.occ}")

    
a=Person("ram","teacher")
a.info()