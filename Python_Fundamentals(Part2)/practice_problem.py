#set1
#1

# n = int(input("Enter the no: "))
# if n%5 == 0:
#     print("Multiple of 5")
# else:
#     print("Not Multiple of 5")

#2

# n = int(input("Enter the no: "))
# status = "Even" if n % 2== 0 else "Odd"
# print(status)

#------------x------------------------------

#set2
#1

# n = int(input("Enter the no: "))
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i+=1

#2

# i = 0
# while i<=10:
#     i+=1
#     if i % 2 == 0:
#         continue
#     print(i)


#3

# word = input("Enter the word: ")
# count = 0
# for i in word:
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':

#     if i in "aeiouAEIOU":
#         count+=1
# print(count)



#4

# n = int(input("Enter the no: "))
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

#---------------x-------------------------

#SET 3
#1

# def factorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f*=i
#     return f

# n = int(input("Enter the no: "))
# print(factorial(n))



#2

# status = lambda a,b,c: max(a,b,c)

def get_largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
a = int(input("Enter the first no: "))
b = int(input("Enter the second no: "))
c = int(input("Enter the third no: "))
print(get_largest(a,b,c))












