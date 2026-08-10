
#*1
# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance

#     def deposit(self,d):
#         if d>0:
#             self.balance +=d
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self,w):
#         if w <= 0:
#             print("Invalid withdraw amount")
#         elif self.balance >= w:
#             self.balance -= w
#             return self.balance
#         else:
#             print("Low balance")

#     def check_balance(self):
#         return self.balance

# b1 = BankAccount("123","jibitesh",500)
# b1.deposit(500)
# print(b1.withdraw(200))
# print(b1.check_balance())



#*2
# class Book:
#     def __init__(self,title,author,list_of_reviews = None):
#         self.title = title
#         self.author = author
#         self.list_of_reviews = list_of_reviews

#     def add_review(self,review):
#         self.list_of_reviews.append(review)

#     def count_reviews(self):
#             return len(self.list_of_reviews)

#     def display_all_reviews(self):
#         return self.list_of_reviews


# b1 = Book("Set T=0","Jibitesh Kumar Mishra",["Great","Outstanding","Fantabulous"])
# b1.add_review("Worth it")
# print(b1.count_reviews())
# print(b1.display_all_reviews())

#*3
# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks

#     def getter(self):
#         return self.__name,self.__roll_no,self.__marks

#     def setter(self,name,roll_no,marks):
#         if marks < 0:
#             print("marks can't be -ve")
#             return
#         elif name == "":
#             print("name can't be empty")
#             return
            
#         elif not(roll_no >=1 and roll_no<=100):
#             print("roll number has to be between 1 & 100")
#             return

#         self.__marks = marks
#         self.__name = name
#         self.__roll_no = roll_no

# s1 = Student("Jibitesh",33,95)
# s1.setter("ankita",21,-2)
# print(s1.getter())


#*4
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):

#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# class Rectangle(Shape):

#     def __init__(self, length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 1/2 *self.base * self.height

# t1 = Triangle(2,5)
# print(t1.area())


#*5
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model


# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)
#         self.seats = seats

#     def __str__(self):
#         return f"Car Brand: {self.brand}, Car Model: {self.model}, no of seats: {self.seats}"


# class Bike(Vehicle):
#     def __init__(self,brand,model,engine_cc):
#         super().__init__(brand,model)
#         self.engine = engine_cc

#     def __str__(self):
#         return f"Bike Brand: {self.brand}, Bike Model: {self.model}, Engine: {self.engine}"

# c1 = Car("Toyata","X12F3","5")
# print(c1)


#*6
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Intern(Employee):
#     def __init__(self,name,id,stipend):
#         super().__init__(name,id)
#         self.stipend = stipend


#     def calculate_salary(self):
#         return self.stipend

# class FullTimeEmployee(Employee):
#     def __init__(self,name,id,monthly_salary):
#         super().__init__(name,id)
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.monthly_salary * 12

# class ContractEmployee(Employee):

#     def __init__(self,name,id,hourly_rate, hours_worked):
#         super().__init__(name,id)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked


# f1 = FullTimeEmployee("Jibitesh","1234",25000000)
# print(f1.calculate_salary())


#*7
# class Person:
#     # def __init__(self,name):
#     #     self.name = name
#     # def __init__(self,name,age):
#     #     self.name = name
#     #     self.age = age


#     def __init__(self,name,age=29,address="14B/2"):
#         self.name = name
#         self.age = age
#         self.address = address

      #*Dunder Method
#     def __repr__(self):
#         return f"{self.name}, {self.age}, {self.address}"

# p1 = Person("Jibitesh",33)
# print(p1)

#*8

# class Player:
#     player_count = 0
#     def __init__(self,name,level):
#         self.name = name
#         self.level = level
#         Player.player_count+=1


# p1 = Player("Jibitesh",20)
# p2 = Player("ankita",33)
# print(Player.player_count)

#*9(MRO-> Method Resolution Order)

# class Herbivore:
#     def __init__(self,plant):
#         self.plant = plant
#     def herbi(self):
#         print(self.plant)

# class Carnivore:
#     def __init__(self,animal):
#         self.animal = animal
#     def carni(self):
#         print(self.animal)

# class Omnivores:
#     def __init__(self,plant,animal):
#         self.plant = plant
#         self.animal = animal

#     def omni(self):
#         print(self.plant,self.animal)

# class Bear(Herbivore,Carnivore,Omnivores):
#     def __init__(self,plant,animal):
#         Herbivore.__init__(self,plant)
#         Carnivore.__init__(self,animal)
#         Omnivores.__init__(self,plant,animal)
#         print(Bear.__mro__)



# b1 = Bear("moneyplant","lion")
# b1.omni()


#*10

class Message:
    message_counter = 1

    def __init__(self,sender,content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter+=1

    def __str__(self):
        return f"({self.id}) {self.sender.username} : {self.content}"

class User:
    def __init__(self,username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.chatroom} cannot send a message (not in a chatroom)")
        else:
            self.chatroom.broadcast(self,content)


class ChatRoom:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        self.users.remove(user)

    def broadcast(self,sender,content):
        message = Message(sender,content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}")
        for msg in self.messages:
            print(msg)

        print()

if __name__ == "main":
    room = ChatRoom("Python Lounge")
    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello Everyone")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hi Alice")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()


    

    

    

    







    


    








    








    
