questions=["1) What does not grow on a tree, according to a popular Hindi saying?,Money , Flowers , Fruits , Leaves ",
           "2) Which city is known as the Pink City of India?, Delhi , Jaipur , Mumbai , Punjab",
           
           ]
 



answers=["A) Money",
         "B) Jaipur "
        
]
x=input("Do you want to play KBC?")
if(x.lower()=="yes"):
    print(questions[0])
    y=input("Enter ans:")
    if(y.lower()=="money"):
        print("you have won 5000")
        print(questions[1])
        z=input("Enter ans:")
        if(z.lower()=="jaipur"):
            print("you have won 10000")
    else:
        print("You lost all money")
            
    

else:
    print("bye")
    

 


