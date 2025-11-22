a=input("Enter a number between 10 and 20:")
if(a.lower()=="quit"):
    exit()
a=int(a)
if (a>=10 or a<=20):
    raise ValueError("No. should be between 10 and 20")