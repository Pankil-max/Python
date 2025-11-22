class Employee:
   
    def __init__(self,name):
        self.name=name      
    def __len__(self):
        i=0
        for c in self.name:
            i+=1;
        return i
    def __str__(self):
        return f"The name of employee is {self.name} (str)"
    def __repr__(self):
        return f"Employee'({self.name})' (repr)"
    def __call__(self):
        print("hey why did u just call me")
    
     

e=Employee("pankil")
print(str(e))

print(len(e)) 
