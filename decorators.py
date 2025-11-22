# def pizza(fx):
#     def add_sausage():
#         print("Add sausage to improve the flavour..")
#         fx()
#         print("Thanks for adding the sausage....")
#     return add_sausage
# def cheezy(fx):
#     def add_cheese():
       
#         fx()
#         print("Successfully added Cheese")
        
#     return add_cheese
    

# @pizza
# @cheezy
# def dish():
#     print("Pizza Ordered")
# dish()


#In this case **kwargs not necessary it should be used when using named args
def greet(fx):
    def say_hello(*args,**kwargs):
        print("This function helps in adding 2 numbers..")
        fx(*args,**kwargs)
        print("Thanks for using the program to add")
    return say_hello

@greet
def add(a,b):
    print(a+b)
add(1,2)