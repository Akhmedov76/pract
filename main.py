from pract.users.admin import add_water, show_all_users, delete_water, edit_water
from pract.users.common import register, login, log_out, UserTypes
from pract.users.logs import log_settings, log_decorator


@log_decorator
def show_auth_menu():
    text = """
    1. Register 
    2. Login
    3. Quit
"""
    print(text)
    user_input = input("Enter your choice: ")
    if user_input == "1":
        if register():
            show_auth_menu()
    elif user_input == "2":
        user = login()
        if not user:
            print("Invalid username and password. Please try again.")
            show_auth_menu()
        elif user['user_type'] == UserTypes.ADMIN.value:
            admin_menu()
        elif user['user_type'] == UserTypes.USER.value:
            show_user_menu()
        else:
            print("Invalid credentials!")
            show_auth_menu()
    elif user_input == "3":
        if log_out():
            print("Goodbye!")
            exit()
        else:
            print("Logout canceled!😊")
            show_auth_menu()
    else:
        print("Invalid input. Please try again.")
        show_auth_menu()


def show_user_menu():
    text = """
    1. Show type of waters
    2. Show my balance  
    3. Exit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Exit successfully!")
            return show_auth_menu()
    except KeyboardInterrupt:
        return show_auth_menu()


@log_decorator
def admin_menu():
    text = """
    1. Add type of waters
    2. Show all users  
    3. Show all order
    4. Quit
"""
    print(text)
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            show_admin_waters()
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            print("Exit successfully!")
            return show_auth_menu()
        else:
            print("\nWrong choice !")
            return admin_menu()
    except KeyboardInterrupt:
        return admin_menu()


def show_admin_waters():
    print("""
1. Add waters
2. Edit waters
3. Delete waters
4. Show all waters menu
5. Exit    
""")
    choice = input("Enter your choice: ")
    if choice == "1":
        if add_water():
            show_admin_waters()
        else:
            print("Invalid credentials!")
            show_admin_waters()
    elif choice == "2":
        if edit_water():
            show_admin_waters()
        else:
            print("Invalid credentials!")
            show_admin_waters()
    elif choice == "3":
        if delete_water():
            show_admin_waters()
        else:
            print("Invalid credentials!")
            show_admin_waters()
    elif choice == "4":
        if show_all_users():
            show_admin_waters()
        else:
            print("Invalid credentials!")
            show_admin_waters()
    elif choice == "5":
        print("Exit successfully!")
        return show_auth_menu()
    else:
        print("\nWrong choice !")
        return admin_menu()


if __name__ == "__main__":
    log_settings()
    show_auth_menu()
