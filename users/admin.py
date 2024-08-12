import random

from file_manager import water_manager, users_manager


class Admin:
    def __init__(self, id, begin, end, comment, price):
        self.id = id
        self.begin = begin
        self.end = end
        self.comment = comment
        self.price = price


def add_water():
    try:
        id = random.randint(1, 100)
        begin = int(input("Enter water start number: "))
        end = int(input("Enter water end number: "))
        comment = input("Enter comment: ").capitalize().strip()
        price = int(input("Enter price: "))
        water = Admin(id, begin, end, comment, price)
        water_manager.add_data(water.__dict__)
        print("Water added successfully!")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def edit_water():
    try:
        id = int(input("Enter water ID to edit: "))
        datas = water_manager.read()
        for water in datas:
            if water['id'] == id:
                water['begin'] = int(input("Enter new water start number: "))
                water['end'] = int(input("Enter new water end number: "))
                water['comment'] = input("Enter new comment: ").capitalize().strip()
                water['price'] = int(input("Enter new price: "))
                water_manager.write(datas)
                print("Water edited successfully!")
                return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_water():
    try:
        id = int(input("Enter water ID to delete: "))
        datas = water_manager.read()
        for water in datas:
            if water['id'] == id:
                datas.remove(water)
                water_manager.write(datas)
                print("Water deleted successfully!")
                return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_all_users():
    try:
        users = users_manager.read()
        if users:
            for user in users:
                print(f"ID: {user['full_name']},\nName: {user['username']},\nEmail: {user['email']},\n")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
