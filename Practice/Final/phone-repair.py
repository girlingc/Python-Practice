# Christian Girling
import re, os, csv
def get_typed_input(prompt = "Enter Value", return_type = "str"):
    # Checking for invalid inputs
    try:
        return eval(return_type)(input(prompt))
    except ValueError:
        # Since the only inputs we are looking for in this program are integers and strings, I am only including these to search for
        if return_type == 'int':
            print('Oops, we were looking for an integer! ')
        elif return_type == 'str':
            print('Oops, we were looking for a string! ')
        else:
            print("Oops, we dont understand what you are typing")
        return get_typed_input(prompt, return_type)

def create_file(file_name):
    with open(file_name, 'w') as f:
        f.write("Model  Serial Number   Owner's Name    Owner's Phone Number    Description of Problem")
        f.close()

def get_owner_info(owner):
    return owner[0] + "(" + str(owner[1]) + ')' + 'from' + str(owner[2]) + '(' + owner[3] + ')', "with" + owner[4]

class Phone:
    def __init__(self, model, serial_number, owner, phone_number, description):
        self.model = model
        self.serial_number = serial_number
        self.owner = owner
        self.phone_number = phone_number
        self.description = description

    def add_phone(self, file_name, model, serial_number, owner, phone_number, description):
        with open(file_name, 'a') as f:
            f.append("{} {}  {}  {}  {}".format(model, serial_number, owner, phone_number, description))

def remove_phone(file_name, model, serial_number, owner, phone_number, description):
    with open(file_name, 'r') as f:
        info = f.readlines()

    with open(file_name, "w") as f:
        for line in info:
            if line.strip("\n") != "{} {}  {}  {}  {}".format(model, serial_number, owner, phone_number, description):
                f.write(line)

def find_phone(file_name, search):
    owners = []
    with open(file_name, newline = '') as f:
        f_reader = csv.reader(f, delimiter = '\t')
        for owner in f_reader:
            if search in owner[2].lower():
                owners.append(owner)
    if owner == []:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are no customers with", search, "in their name.")
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
    # Printing list of titles, as well as their respective authors and dates published
    else:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are", len(owners), "phones from an owner with", search, "in their name:")
        print('')
        print('\n'.join(map(get_owner_info, owners)))
        print('')
        print('-----------------------------------------------------------------------------------')

def list_phones(file_name):
    owners = []
    with open(file_name, newline = '') as f:
        f_reader = csv.reader(f, delimiter = '\t')
        for owner in f_reader:
            owners.append(owner)
    if owner == []:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("We currently have no customers")
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
    # Printing list of titles, as well as their respective authors and dates published
    else:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are", len(owners), "customers")
        print('')
        print('\n'.join(map(get_owner_info, owners)))
        print('')
        print('-----------------------------------------------------------------------------------')

    

def print_dashboard():
    create_file('phones.txt')
    # Printing the user interface
    print("""
    Please choose an option
    1: Add your phone
    2: Remove your phone
    3: Find your phone
    4: List all phones
    
    Q: Quit
    """)


    # Obtaining what function the user wants to input
    user_selection = input(" ")
    
    if user_selection == "1":
        print("List your information below: ")
        model = get_typed_input("Model: ", 'str')
        serial_number = get_typed_input("Serial Number: ", 'str')
        owner = get_typed_input("Owner's name: ", 'str')
        phone_number = get_typed_input("Owner's Phone Number: ", 'str')
        description = get_typed_input("Description of the problem: ")
        Phone(model, serial_number, owner, phone_number, description).add_phone(owner, 'phones.txt', model, serial_number, owner, phone_number, description)
        return True

    elif user_selection == "2":
        print("List your information below: ")
        model = get_typed_input("Model: ", 'str')
        serial_number = get_typed_input("Serial Number: ", 'str')
        owner = get_typed_input("Owner's name: ", 'str')
        phone_number = get_typed_input("Owner's Phone Number: ", 'str')
        description = get_typed_input("Description of the problem: ")
        remove_phone('phones.txt', model, serial_number, owner, phone_number, description)
        return True

    elif user_selection == "3":
        search = get_typed_input("What is the owner's name? ", 'str').lower()
        find_phone('phones.txt', search)
        return True
    
    elif user_selection == "4":
        list_phones('phones.txt')
        return True


    elif user_selection == "5":
        print("Thank you for using my program :)")
        return False
    
    else:
        print("Please choose either 1, 2, 3, 4 or press 5 to quit")
        return True


def main():
    program_running = True

    while program_running:
        program_running = print_dashboard()

if __name__ == "__main__":
    main()