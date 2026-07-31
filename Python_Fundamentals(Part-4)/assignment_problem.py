
#*1
class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,d):
        if d>0:
            self.balance +=d
        else:
            print("Invalid deposit amount")

    def withdraw(self,w):
        if w <= 0:
            print("Invalid withdraw amount")
        elif self.balance >= w:
            self.balance -= w
            return self.balance
        else:
            print("Low balance")

    def check_balance(self):
        return self.balance

b1 = BankAccount("123","jibitesh",500)
b1.deposit(500)
print(b1.withdraw(200))
print(b1.check_balance())