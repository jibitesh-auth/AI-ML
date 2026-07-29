# class Employee:
#     start_time ="10am"
#     end_time = "6pm"

#     def change_time(self,new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self,subject):
#         self.subject = subject


# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role = role

# t1 = Teacher("Math")
# t1.change_time("5pm")
# print(t1.subject,t1.start_time,t1.end_time)

# staff1 = AdminStaff("Manager")
# print(staff1.role)

#-----------------------x---------------------------------------

#*Multi Level Inheritance

# class Employee:
#     start_time ="10am"
#     end_time = "6pm"


# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary = salary

# staff1 = AdminStaff("Manager")
# print(staff1.role)

# acc1 = Accountant(25_000, "CA")
# print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)

#----------------------x----------------------------------------

#*Multiple Inheritance

class Teacher:
    def __init__(self,salary):
        self.salary = salary


class Student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary) #using super
        Student.__init__(self,gpa) #usinig class name
        self.name = name

ta1 = TA(15_000, 9.3,"Jibitesh")
print(ta1.salary,ta1.gpa,ta1.name)
    





