with open("sample.txt","r") as f:
    data = list(f.readlines())
    a = False
    line = 0
    for i in data:
        if "\n" in i:
            line+=1
        if "Python" in i:
           print("Exist")
           print(f"Line: {line}")
           a = True
           break

    if a == False:
        print("Doesn't Exist")
    



#*OR


data = True
line = 1
word = "Python"

with open("sample.txt","r") as f:
    while data:
        data = f.readline()

        if word in data:
            print(f"{word} found at line {line}")
            break

        line+=1


