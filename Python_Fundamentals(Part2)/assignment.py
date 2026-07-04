#1
# salary = float(input("Enter the salary: "))
# if salary < 30000:
#     tax = salary * 0.05
# elif salary >= 30000 and salary < 70000:
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
# def right_print(n):
#     a = ''
#     while n>0:
#         last_digit = n % 10
#         a+=str(last_digit)
#         n//=10
#     for i in range(len(a)-1, -1, -1):
#         print(a[i])
    

# right_print(312)