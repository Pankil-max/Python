# Seek(5) fun is used while we dont need to read file from first here first it takes 5 characters tan only read first 5 are not read
# tell() is used how many cbytes are there
# truncate(5) is used to store limited chars in this case first 5 char are saved

with open("file3.txt","w") as f:
    f.write("123456789tet")
    f.truncate(5)


with open("file3.txt","r")as f:
    # f.seek(10)
    d= f.read()
    print(d)


    print(f.tell())
