#1
# salary = float(input("Enter the salary: "))
# if salary < 30000:
#     tax = salary * 0.05
# elif salary <= 70000:
#     tax = salary * 0.15
# else:
#     tax = salary * 0.25

# print(tax)

#2
# def even_num(a,b):
#     for i in range(a,b+1):
#         if i % 2==0:
#             print(i)

# a = int(input("Enter the first no: "))
# b = int(input("Enter the second no: "))
# even_num(a,b)

#3
# def digits(n):
#     while n>0:
#         last_digit = n%10
#         print(last_digit)
#         n//=10
    
# digits(312)

#4
# def count(n):
#     c = 0
#     while n>0:
#         last_digit =n%10
#         n//=10
#         c+=1
#     return c

# n = int(input("Enter the no: "))
# print(count(n))

#5
# def sum(n):
#     s = 0
#     while n>0:
#         last_digit =n%10
#         s+=last_digit
#         n//=10
        
#     return s

# n = int(input("Enter the no: "))
# print(sum(n))

#6
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)

#OR

#for i in range(15,101,15):
#   print(i)

#7
# while True:
#     a = input("Enter the no: ")
#     if a == 'Quit':
#         break
#     elif int(n) > 0:
#          print("Positive")
#     elif int(n) < 0:
#          print("Negative")
#     else:
#          print("Wrong Input")

#8
# def calculator(a,b,operation):
#     match operation:
#         case '+':
#             return a+b
#         case '-':
#             return a-b
#         case '*':
#             return a*b
#         case '/':
#             return a/b
#         case _:
#             return "Invalid value"
        
# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))
# c = input("Enter the Operation: ")
# print(calculator(a,b,c))

#9
# def is_prime(n):
#     if n<2:
#         return False
#     if n==2:
#         return True
#     for i in range(2,n):
#         if n%i == 0:
#             return False
    
#     return True


# n = int(input("Enter the no: "))
# print(is_prime(n))

#10
# secret_no = 10
# a = int(input("Guess the no: "))
# if a>secret_no:
#     print("Too high")
# elif a<secret_no:
#     print("Too low")
# else:
#     print("Correct!")


   
