import math

def get_typed_input(prompt = "Enter Value", return_type = "str"):
    # Checking for invalid inputs
    try:
        return eval(return_type)(input(prompt))
    except ValueError:
        print("Oops, please enter a", return_type)
        return get_typed_input(prompt, return_type)


def sum_and_average():
    print("Please enter two numbers")

    # Obtaining the variables (num1 and num2)
    num1 = get_typed_input("First Number: ", "float")
    num2 = get_typed_input("Second Number: ", "float")

    # Calculating the sum and the average of the numbers
    sum_numbers = (num1 + num2)
    average = ((num1 + num2)/2)

    print(f"The sum of the two numbers is: ", sum_numbers)
    print("The average of the two numbers is: %.2f " % average)
    return


def minimum_and_maximum():
    # Creating a list of 5 numbers
    numbers = []

    for i in range(1, 6):
        number = get_typed_input("Enter number: ", 'float')

        # Adding the inputed numbers into the list
        numbers.append(number)

    # Calculating the maximum and the minimum
    minimum = min(numbers)
    maximum = max(numbers)

    print("The minimum number is: %.2f" % minimum)
    print("The Maximum number is: %.2f" % (maximum))
    return


def area_and_perimeter():
    print("Please enter the lengths of the two sides of the rectangle")
    # Obtaining the two sides of the rectangle

    side1 = get_typed_input("Side 1: ", 'float')
    side2 = get_typed_input("Side 2: ", 'float')
    
    # Calculating the area and the perimeter of the rectangle 
    area = (side1 * side2)
    perimeter = (2 * side1) + (2 * side2)
    

    print("The area of the rectangle is: %.2f" % area)
    print("The perimeter of the rectangle is: %.2f" % perimeter)
    return


def sum_and_product():
    # Obtaining the amount of natural numbers to be calculated
    n = get_typed_input("Enter number of natural numbers: ", 'int')

    # Calculating the sum and the product of the list of natural numbers
    print(sum(list(range(n + 1)[1:])))
    print(math.prod(list(range(n + 1)[1:])))


def string_info():
    # Obtaining the string
    phrase = input("Please input a string: ")

    # Returning a list of words in the string 
    number_words = len(phrase.split())

    print("Number of characters: ", len(phrase))
    print("Number of words: ", number_words)
    return
    

def calculator(total = 0, last_operator = ''):
    # Obtaining a number
    number = None
    while number is None:
        number = get_typed_input("Please input a number: ", 'float')
        if last_operator == '/' and number == 0:
            number = None
            print('Can\'t divide by Zero.')

    # Obtaining an operator
    operator = None
    while not operator in ['+', '-', '/', '=']:
        operator = get_typed_input('Enter an operator ("+", "-", "/", "*") | Enter "=" to complete: ')

    # Operator is only empty on initial call
    if last_operator == '':
        return calculator(number, operator)

    # Executing the operator
    if last_operator == '+':
        total += number
    if last_operator == '-':
        total -= number
    if last_operator == '/':
        total /= number
    if last_operator == '*':
        total *= number

    print('SubTotal: ', total)

    # Finishing the loop
    if operator == '=':
        return total
    else:
        return calculator(total, operator)
    

def print_dashboard():
    # Printing the user interface
    print("[1] Sum and Average of Two Numbers")
    print("[2] Maximum and Minimum of 5 Numbers")
    print("[3] Area and Perimeter of a Rectangle")
    print("[4] Sum and Product of first N Natural Number")
    print("[5] String Info")
    print("[6] Calculator")
    print("")
    print("[0] Exit")

    # Obtaining what function the user wants to input
    user_selection = input("What function do you want to choose? ")
    
    if user_selection == "1":
        sum_and_average()
        return True

    elif user_selection == "2":
        minimum_and_maximum()
        return True

    elif user_selection == "3":
        area_and_perimeter()
        return True
    
    elif user_selection == "4":
        sum_and_product()
        return True

    elif user_selection == "5":
        string_info()
        return True

    elif user_selection == "6":
        print(calculator())
        return True
    
    elif user_selection == "0":
        print("Thank you for using my program :)")
        return False
    
    else:
        print("Please choose either [1], [2], [3], [4], [5] or [0]")
        return True


def main():
    program_running = True

    while program_running:
        program_running = print_dashboard()



if __name__ == "__main__":
    main()