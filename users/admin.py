"""
    1. Add type of waters
    2. Show all users
    3. Quit
"""
from pract.file_manager import water_manager


class Admin:
    def __init__(self, begin, end, price):
        self.begin = begin
        self.end = end
        self.price = price


def add_water():
    try:
        begin = int(input("Enter water start number: "))
        end = int(input("Enter water end number: "))
        price = float(input("Enter price: "))
        water = Admin(begin, end, price)
        water_manager.add_data(water.__dict__)
        print("Water added successfully!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
