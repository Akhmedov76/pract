"""
    1. Add type of waters
    2. Show all users
    3. Quit
"""


class Admin:
    def __init__(self, count, price):
        self.count = count
        self.price = price
        self.users = []


def add_water():
    water_type = input("Enter water type: ")
    count = int(input("Enter count: "))
    price = float(input("Enter price: "))
    admin = Admin(count, price)
    admin.users.append({"water_type": water_type, "count": count, "price": price})
    print("Water added successfully!")
