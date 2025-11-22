
try:
    a=int(input("Enter  a number:"))
    print(f"The multiplication of {a} is :")
    for i in range(1,11):
        print(f"{a}*{i}={a*i}")
except ValueError as e:
    print(e,"(error)")
    print("Try entering digit only")

print("This is the basic code")
print("YOU HAVE SUCCESSFULLY COMPLETED THE CODE")