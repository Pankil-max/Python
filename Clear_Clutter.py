import os 

files=os.listdir("PNG_FILES")
i=1
for file in files:
    if file.endswith("png"):
        print(f"{file}")
        os.rename(f"PNG_FILES/{file}",f"PNG_FILES/{i}.png")
        i+=1
renamed_files=os.listdir("PNG_FILeS")
for file in renamed_files:
    print(f"{file}")