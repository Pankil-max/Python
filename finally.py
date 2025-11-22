def func():
    try:
        x=int (input("Enter a number:"))
        l=[1,2,3,4,5]
        print(l[x])
        return 1 
    except ValueError as e :
        print("Enter  no")
        return -1
    except IndexError as e :
        print("Invalid Index")
        return -1
    finally:
        print("Always executed")


x=func()
print("Returned value:",x)



