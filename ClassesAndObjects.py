class Person:
    name="Ram"
    occupation="Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

    
a=Person()
a.name="Shyam"
a.occupation="Professor"
b=Person()
b.name="Sita"
b.occupation="bgnessman"
a.info()
b.info()
