# f=open("myfile2.txt","w")
# txt=f.write("HEllo this is second line ")
# print(txt)
# f.close()

# with open() keyword is used to read or write or append without requring a file to close

with open("myfile.txt","a") as f:
    f.write("hey this line is written using with open keyword")
