from pract.users.common import register, login, log_out
from pract.users.logs import log_settings


def show_auth_menu():
    text = """
    1. Register 
    2. Login
    3. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            if register():
                show_auth_menu()
            else:
                return show_auth_menu()
        elif user_input == "2":
            if login():
                show_auth_menu()
            else:
                print("Error")
                show_auth_menu()
        elif user_input == "3":
            if log_out():
                print("Goodbye!")
                exit()
        else:
            print("\nWrong choice !")
            return show_auth_menu()
    except KeyboardInterrupt:
        return show_auth_menu()


def show_menu():
    text = """
    1. Show type of waters
    2. Show my balance  
    3. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("\nThakns for wisit")
            exit()
    except KeyboardInterrupt:
        return show_menu()


def admin_menu():
    text = """
    1. Add type of waters
    2. Show all users  
    3. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("\nThakns for wisit")
            exit()
        else:
            print("\nWrong choice !")
            return admin_menu()
    except KeyboardInterrupt:
        return admin_menu()


if __name__ == "__main__":
    log_settings()
    show_auth_menu()
