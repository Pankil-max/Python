x=4 #This is global variable
def  Hello():
    #To modify global variable inside a function use global keyword
    x=3 # This is local variable
    print(f"The local variable is {x}")

    print("Hi Pankil")
Hello()
print(f"The global variable is {x}")
