from car import *
globvar = 0
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


def print_dashboard():
    # Printing the user interface
    print("""
    ==============================
    Choose 1-6 or 0 to exit
    ------------------------------
    [1] Create the car object
    [2] List the car's details
    [3] Display the car's profit
    [4] Reduce the car's price

    [5] Delete the car object

    [6] Test - create car1 and car2 

    [0] Exit
    ==============================
    """)
    # Obtaining what function the user wants to input
    user_selection = input("What function do you want to choose? ")
    
    if user_selection == "1":
        global globvar
        globvar = (get_typed_input("Enter the make of the car: ", "str"), get_typed_input("Enter the model of the car: ", "str"), get_typed_input("Enter the year of the car: ", "int"), get_typed_input("Enter the cost of the car: ", "float"), get_typed_input("Enter the price of the car: ", "float"))
        return True

    elif user_selection == "2":
        Car.get_details(globvar)
        return True

    elif user_selection == "3":
        Car.calc_profit(globvar)
        return True
    
    elif user_selection == "4":
        Car.reduce_price(globvar, 5000)
        return True

    elif user_selection == "5":
        Car.__del__(globvar)
        return True

    elif user_selection == "0":
        print("Thank you for using my program :)")
        return False
    
    else:
        print("Please choose either [1], [2], [3], [4], or [0]")
        return True


def main():
    program_running = True

    while program_running:
        program_running = print_dashboard()


if __name__ == "__main__":
    main()