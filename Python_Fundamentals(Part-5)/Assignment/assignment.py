
#*1
# with open("names.txt","w") as f:
#     k = 1
#     for i in range(5):
#         text = input(f"Enter the {k} line: ")
#         f.write(text + "\n")
#         k+=1

# with open("names.txt","r") as f:
#     data = f.read()
#     print(data)

#*2
# with open("log.txt",'a') as f:
#     f.write("Program run successfully")

# with open("log.txt",'r') as f:
#     print(f.read())

#*3
# num = [5,10,15,20,25]
# new = []
# data = [new.append(i) for i in num if i>15]
# print(new)

#*4
import json

with open("cities.json",'w') as f:
    data = {
        "Rourkela": 54356,
        "Mumbai": 43434,
        "Kerela": 343434
    }
    json.dump(data,f,indent=4,sort_keys=True)

with open("cities.json",'r') as f:
    data = json.load(f)
    print(data)

new_city = input("Enter new city:")
population = int(input("Enter the population: "))
data.update({new_city : population})

with open("cities.json",'w') as f:
    json.dump(data,f, indent=4, sort_keys=True)
 

#*5
# try:
#     with open("data.txt","r") as f:
#         data = f.read()
# except Exception as e:
#     print(e)
#     print("File not found!")
# else:
#     print(data)





