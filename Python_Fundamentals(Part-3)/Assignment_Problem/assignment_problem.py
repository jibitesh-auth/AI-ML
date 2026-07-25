
#*1

# str = input("Enter the String: ")
# str1 = str[::-1]
# if str1 == str:
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")


# str = input("Enter the String: ")
# str1=""
# for ch in range(len(str) -1, -1,-1):
#     str1 += str[ch]
# if str1 == str:
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")


#*2

# list = [1,5,4,7,8]
# sum = 0
# for i in list:
#     sum += i
# avg = sum/len(list)
# print(avg)



#*3

# list1 = []
# list2 = []
# a = int(input("Enter length of list1: "))
# b = int(input("Enter length of list2: "))
# for i in range(a):
#     list1.append(int(input("Enter the no: ")))

# for i in range(b):
#     list2.append(int(input("Enter the no: ")))

# list = []
# list = list1 + list2
# list.sort()
# print(list)

#*4

# tup = (1,2,3,4,5)
# list1 = []
# list2 = []
# for i in tup:
#     if i%2==0:
#         list1.append(i)
#     else:
#         list2.append(i)

# print(tuple(list1))
# print(tuple(list2))

#*5

dict = {}
ch = input("Enter A, B, C, D:\nA-Add a Student\nB-Update Marks\nC-Search for a Student\nD-Display all Students and Marks\n").upper()

match ch:
    case 'A':
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        dict.update({name:marks})
    case 'B':
        name = input("Enter name- marks to be edited")
        marks = int(input("Enter marks: "))
        # if name in dict.keys():
        if name in dict:
            dict[name] = marks
        else:
            print("Invalid data")
    case 'C':
        name = input("Enter name: ")
        if name in dict:
            print(f"{name} present")
        else:
            print(f"{name} not present")
    case 'D':
        print(dict.items())
    case _ :
        print("Invalid")

        
        










