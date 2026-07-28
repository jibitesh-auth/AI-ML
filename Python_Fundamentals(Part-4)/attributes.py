class Student:
    college_name = "ABC college"#class
    PI = 3.1

    def __init__(self,name,gpa): 
        self.name = name  #instance
        self.gpa = gpa
        self.PI = 3.14


stu1 = Student("Rahul",9.2)
print(stu1.name)
print(Student.college_name) #can be invoked from both class & object name
print(stu1.college_name)

print(stu1.PI)
print(Student.PI)
