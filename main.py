


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
           pass
        elif user_input == "3":
            print("\nThakns for wisit")
            return
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
        elif user_input == "6":
            print("\nThakns for wisit")
        else:
            print("\nWrong choice !")
            return show_menu()
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
        elif user_input == "6":
            print("\nThakns for wisit")
        else:
            print("\nWrong choice !")
            return admin_menu()
    except KeyboardInterrupt:
        return admin_menu()


if __name__ == "__main__":
   show_auth_menu()