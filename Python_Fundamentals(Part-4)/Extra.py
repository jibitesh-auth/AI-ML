class Solution:
    a = 5
    def __init__(self):
        self.b = 7

s1 = Solution()
s2 = Solution()
# Solution.a+=1 
# print(s1.a)
# print(s2.a)

s1.b+=1
print(s1.b,s2.b)
