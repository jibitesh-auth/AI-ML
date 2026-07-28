# Product store
# Design & create an online store for Products (name, price).

# Track total products being created.

# Create a static method to calculate discount on each product based on a % parameter.

#-------------------x--------------------------------------------

class Product_Store:
    count = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product_Store.count+=1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")


    @classmethod
    def prod_count(cls):
        print(f"total products in store = {cls.count}")

    @staticmethod
    def cal_discount(price,percentage):
        final_price = price - (percentage * price /100)
        print(f"Final Price = {final_price}")



p1 = Product_Store("a",25)
p2 = Product_Store("b",456)

Product_Store.prod_count()
p1.cal_discount(p1.price,30)


    
    