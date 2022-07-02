# 8 inch by 50.5

def dimensions_rectangle():
    side1 = input("What is the first side of the rectangle (inches(? ")
    side2 = input("What is the second side of the rectangle (inches)? ")
    area = side1 * side2
    floor_boards = area
    print("The amount of floor boards is", floor_boards)
    

def dimensions_not_rectangle():
    sides = input("How many sides are there to the room?")
    if sides == 3:
        input("What is the length of the first side?")
        input("What is the length of the second side?")
        input("What is the length of the third side?")
    elif sides == 4:
        input("What is the length of the first side?")
        input("What is the length of the second side?")
        input("What is the length of the third side?")
        input("What is the length of the fourth side?")
    elif sides == 5:
        input("What is the length of the first side?")
        input("What is the length of the second side?")
        input("What is the length of the third side?")
        input("What is the length of the fourth side?")
        input("What is the length of the fifth side?")

    


def print_dashboard():
    # Printing the user interface
    print("[2] Floor boards if you know dimensions if rectangle(square foot)")
    print("[3] Floor boards if you know the dimensions and not rectangle")
    print("")
    print("[0] Exit")

    # Obtaining what function the user wants to input
    user_selection = input("What function do you want to choose? ")
    

    if user_selection == "2":
        dimensions_rectangle()
        return True

    elif user_selection == "3":
        dimensions_not_rectangle()
        return True
    
    elif user_selection == "0":
        print("Thank you for using my program :)")
        return False
    
    else:
        print("Please choose either [1], [2], [3] or [0]")
        return True


def main():
    program_running = True

    while program_running:
        program_running = print_dashboard()



if __name__ == "__main__":
    main()