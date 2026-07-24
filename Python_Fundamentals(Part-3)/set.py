s = {1,2,2,3,3,3}
# print(s)
# print(type(s))
#*O/P: <class 'set'>

# print(len(s))

#---------------x----------------

# s.add(5)
# print(s)

#-----------------x---------------

# empty_set = {}
# print(type(empty_set))
#*<class 'dict'>

# empty_set = set()
# print(type(empty_set))

#----------------x---------------------

#*METHODS

#*1) s.add(val)

# s.add(5)
# print(s)

#*2) s.remove(val)

# s.remove(1)
# print(s)

#*3) s.clear()

# s.clear()
# print(s)
#Output: set()

#*4) s.pop()

# s.pop()
# print(s)

#*5,6) s.union(set2), s.intersection(set2)

s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}
print(s1.union(s2))
print(s1.intersection(s2))
