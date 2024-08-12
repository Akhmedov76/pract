import os
import json
import random

class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_exists_and_not_empty(self):
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read(self):
        if self.file_exists_and_not_empty():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def write(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def add_data(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        self.write(all_data)
        return "Data added successfully"


    def get_active_user(self):
        all_users: list = self.read()
        try:
            for user in all_users:
                if user['is_login']:
                    return user
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False


    def random_id(self):
        try:
            all_data: list = self.read()
            while True:
                random_number: int = random.randint(1, 9999)
                for data in all_data:
                    if data['id'] == random_number:
                        break
                return random_number
        except Exception as e:
            print(f'Error asad: {e}')
            return False


balance_manager = JsonManager("pract/datas/water.json")
users_manager = JsonManager("pract/datas/users.json")
water_manager = JsonManager("pract/datas/water.json")