class Student:

    def __init__(self): #default
        print("obj is beinig constructed..")

    def __init__(self,name, cgpa):#Parameterized(considered)
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Rahul",9)
stu2 = Student("Jibitesh",8.5)
stu3 = Student("Ankita",10)

print(stu3.name)
print(stu3.cgpa)
print(stu2.name)

print(f"{stu3.name} has a cgpa of {stu3.get_cgpa()}")

