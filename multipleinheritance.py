class Fruits:
    def __init__(self,name):
        self.name=name;
    def show(self):
        print(f"Fruits name is{self.name}")
    

class Color:
    def __init__(self,color):
        self.color=color
    
class taste(Fruits, Color):
    def __init__(self, name, taste):
        self.name = name   
        self.taste = taste


t1=taste("Apple","Sweet")
t1.show()
print(t1.taste)


        
        


        