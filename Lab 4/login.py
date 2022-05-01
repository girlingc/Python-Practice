import re
def generate_login():
    first_name = str(input('Enter your first name: '))
    last_name = str(input('Enter your last name: '))
    bcit_id = str(input("Enter your BCIT ID: "))
    login = str(first_name.strip().capitalize()[0:3]) + str(last_name.strip().capitalize()[0:3]) + str(bcit_id.lower()[-3:])
    return login


def change_password():
    is_valid = False
    while not is_valid:
        password = input("Enter a new password: ")
        errors = []
        if not re.search("[A-Z]", password):
            errors.append("The password must have at least uppercase character")
        if not re.search("[a-z]", password):
            errors.append("The password must have at least lowercase character")
        if len(password) < 7:
            errors.append("The length of the passward must be 7 characters or more")
        if len(errors) == 0:
            is_valid = True
        else:
            for error in errors:
                print(error)
    return password

def print_dashboard():
    print("[1] Create Username")
    print("[2] Change Password")
    print("")
    print("[0] Exit")


    user_selection = input("What function do you want to choose? ")

    if user_selection == "1":
        print(generate_login())
        return True
    
    elif user_selection == "2":
        print(change_password())
        return True

    elif user_selection == "0":
        return False
    else:
        print("Please choose either [1], [2], or [0]")
        return True
        

def main():

    program_running = True

    while program_running:
        program_running = print_dashboard()


if __name__ == '__main__':
    main()