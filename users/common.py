import hashlib
from datetime import datetime
from enum import Enum
from file_manager import users_manager
from users.logs import log_decorator

Admin_login = "Admin"
Admin_password = "admin"


class UserTypes(str, Enum):
    ADMIN = "Admin"
    USER = "user"


class User:
    def __init__(self, full_name, username, email, password, date):
        self.full_name = full_name
        self.email = email
        self.username = username
        self.password = password
        self.date = date
        self.is_login = False

    def check_password(self, confirm_password):
        return confirm_password == self.password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_username(username: str):
        all_users = users_manager.read()
        for user in all_users:
            if user['username'] == username:
                return username


def check_email(email):
    if '@' in email:
        return True
    return False


def register() -> bool:
    try:
        full_name = input("Enter your full name: ").title().strip()
        username = input("Enter username: ").capitalize().strip()
        if User.check_username(username):
            print("Username already exists")
            return register()
        gmail = input("Enter email address: ").strip().lower()
        if not check_email(gmail):
            print("Invalid email address")
            return register()
        password = input("Enter your password: ").strip()
        confirm_password = input("Enter your confirm password: ")
        date = str(datetime.now())
        users = User(full_name, username, gmail, password, date)
        if not users.check_password(confirm_password):
            print("Passwords do not match")
            return register()
        users.password = User.hash_password(password)
        users_manager.add_data(data=users.__dict__)
        print("🎉Successfully registered🎉")
        return True

    except Exception as e:
        print(f"Something went wrong {e}")
    return False


def find_user(username, password):
    all_users = users_manager.read()
    for user in all_users:
        if user['username'] == username and user['password'] == password:
            return True
    return False


@log_decorator
def login() -> dict[str, str] | bool:
    username = input("Enter username: ").capitalize().strip()
    password = input("Enter your password: ").strip()
    hashed_password = User.hash_password(password)
    if username == Admin_login and password == Admin_password:
        print("Welcome to Admin👮‍♂️")
        return {'user_type': UserTypes.ADMIN.value}
    elif find_user(username, hashed_password):
        data = users_manager.read()
        for user in data:
            if user['username'] == username and user['password'] == hashed_password:
                user['is_login'] = True
                users_manager.write(data)
                print(f'Welcome to the user menu: {username}🎉')
        return {'user_type': UserTypes.USER.value}
    else:
        return False


def log_out():
    try:
        txt = """
Are you sure you want to exit😱? Yes or No
        """
        print(txt)
        choice = (input("Enter your answer: ").lower())
        if choice == "yes":
            read = users_manager.read()
            for user in read:
                user["is_login"] = False
                users_manager.write(read)
            return True
        else:
            print("Exit cancelled.")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


@log_decorator
def logout(self) -> bool:
        try:
            all_users: list = users_manager.read()
            for user in all_users:
                user['is_login'] = False
            users_manager.write(all_users)
            return True
        except ValueError:
            return True