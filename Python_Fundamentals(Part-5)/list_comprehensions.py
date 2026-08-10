
#*Without List_Comprehension
# square = []
# for i in range(6):
#     square.append(i*i)
# print(square)

#*With List_Comprehension
# square = [i*i for i in range(6)]
# print(square)

#*List_Comprehension(using condition)
# square = [i*i for i in range(6) if i%2 != 0]
# print(square)

#*[-2,-4,3,5,2,-1]  -> Convert negative to 0

# nums = [-2,-4,3,5,2,-1]
# nums = [ 0 if val < 0 else val for val in nums]
# print(a)

#---------------x-------------------------------------

# words = ["hello", "python" , "apnacollege"]
# print(words[0].upper())
# words = [val.upper() for val in words]
# print(words)






 