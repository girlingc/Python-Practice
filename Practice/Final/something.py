# Christian Girling
import re

def split_numbers():
    # Initial String
    numbers = "1,2,3,4,5,6,7,8,9,10"

     # Splitting the string using Regular Expressions
    numbers_re = re.split(",", numbers)
    print(numbers_re)
    print(set(numbers_re))
    print(tuple(map(int, numbers_re)))

   # Splitting the string using a string method
    numbers_string = numbers.split(",")
    print(numbers_string)
    print(set(numbers_string))
    print(tuple(map(int, numbers_string)))

def hello_or_bye(input1, input2, input3, input4):
    # If statement that says that input1 has to equal input2, the same for input3 and input4
    if input1 == input2 and input3 == input4:
        print("Hello")
    else: print("Bye")

def count_to_hundred():
    # The number starts at 0
    number = 0
    # Adding list of numbers to skip
    skip_number = [7, 17, 27]
    # While loop to count to 100
    while number <= 99:
        number = number +1
        # Implementing code to skip the list of numbers
        if number == skip_number[0] or number == skip_number[1] or number == skip_number[2]:
            continue
        print(number)

def add_to_number(input1):
    # For loop which adds 5 to the parameter a total of 20 times
    """ Returns input1 + (5*20)"""
    for i in range(20):
        input1 = input1 + 5
        print(input1)
    return input1

def get_max_min_count_sum(list1):
    """ List1: Either a manually inputted list, or a list provided
        return: Returns the max, min, count, and sum of the numbers in the list
        """
    numbers = list1
    max = numbers[0]
    min = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number
    count = len(numbers)
    sum_numbers = sum(numbers)
    print("The maximum number in this list is:", max)
    print("The minimum number in this list is:", min)
    print("The count of the list is:", count)
    print("The sum of these numbers is:", sum_numbers)
    return max, min, count, sum_numbers


def get_typed_input(prompt = "Enter Value", return_type = "str"):
    # Checking for invalid inputs
    """ prompt: Acquires the value of the input
        return_type: Acquires the desired type of input
        return: Returns the value, return type, and enters it into the variable
        """
    try:
        return eval(return_type)(input(prompt))
    except ValueError:
        # Since the only inputs we are looking for in this program are integers and strings, I am only including these to search for
        if return_type == 'int':
            print('Oops, we were looking for an integer! ')
        elif return_type == 'str':
            print('Oops, we were looking for a string! ')
        elif return_type == 'float':
            print('Oops, we were looking for a float! ')
        else:
            print("Oops, we don't understand what you are typing")
        return get_typed_input(prompt, return_type)


def main():
    split_numbers()
    hello1 = get_typed_input("Choose an integer: ", 'int')
    hello2 = get_typed_input("Choose an integer: ", 'int')
    hello3 = get_typed_input("Choose an integer: ", 'int')
    hello4 = get_typed_input("Choose an integer: ", 'int')
    hello_or_bye(hello1, hello2, hello3, hello4)
    count_to_hundred()

    add_to_number(get_typed_input("What number would you like to add 5 to 20 times?", 'int'))
    max_min_choice = get_typed_input("Would you like to create a list of 10 floats? [y/n] ", "str")
    if max_min_choice == 'y':
        a = get_typed_input("Float 1: ", "float")
        b = get_typed_input("Float 2: ", "float")
        c = get_typed_input("Float 3: ", "float")
        d = get_typed_input("Float 4: ", "float")
        e = get_typed_input("Float 5: ", "float")
        f = get_typed_input("Float 6: ", "float")
        g = get_typed_input("Float 7: ", "float")
        h = get_typed_input("Float 8: ", "float")
        i = get_typed_input("Float 9: ", "float")
        j = get_typed_input("Float 10: ", "float")
        get_max_min_count_sum([a,b,c,d,e,f,g,h,i,j])
    if max_min_choice == 'n':
        get_max_min_count_sum([-3.5, 0, 235.90, 5, 100.50])
    else:
        print("Please enter either 'y' or 'n' ")

if __name__ == "__main__":
    main()