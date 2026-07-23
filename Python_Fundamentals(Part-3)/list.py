# marks = [99,89,100,65,92]
# print(marks)
# print(len(marks))
# print(marks[1])
# print(marks[9])
# print(marks[len(marks) - 1])

# marks[2] = 70
# print(marks)


# marks = [99,89,100,65,92, "abc", 100.99]
# print(type(marks))

#Slicing
# marks = [99,89,100,65,92, "abc", 100.99]
# print(marks[:5])
# print(marks[5:])
# print(marks[-5:-2])


#-------------------x-------------------------
#append
# nums = [1,2,3]
# nums.append(4)
# print(nums)

#insert
# nums = [1,2,3]
# nums.insert(2,5)
# print(nums)

#SORT
# nums = [1,10,5,6]
# nums.sort()
# nums.sort(reverse= True)
# print(nums)

#Reverse
# nums = [1,2,10,3,4]
# nums.reverse()
# print(nums)

#--------------------x-------------------------------------

#Loops
# nums = [1,2,3,10,4]
# for val in nums:
#     print(val)


#Linear Search
nums = [1,2,3,10,4]

x = 10
idx = 0
for val in nums:
    if val == x:
        print(f"{x} found at idx = {idx}")
        break
    idx+=1
