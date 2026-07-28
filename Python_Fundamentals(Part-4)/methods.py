class Laptops:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def cal_discount(price,discount):
        final_price = price - (discount * price/100)
        print(f"final price = {final_price}")

l1 = Laptops("16gb", "512gb")
l2 = Laptops("8gb", "256gb")

l1.get_info()
Laptops.get_storage_type()
l1.get_storage_type()
l1.cal_discount(40_000, 10)