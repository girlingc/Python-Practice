import re
import random
import string

def counting_items():
    oceans = ["pacific", "atlantic", "arctic", "indian"]
    number_of_oceans = len(oceans)
    return number_of_oceans

def calculate_BMI():
    user_weight = float(input("enter weight in Kilograms: "))
    user_height = float(input("enter height in Metres: "))
    BMI_formula = user_weight / (user_height*user_height)
    return BMI_formula

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

occupation = {"Hannah": "rock climber", "Nick":"artist", "Shawn":"software developer", "Emily":"Unemployed"}
def display_all_careers(occupation):
    result = ''
    for key, value in occupation.copy().items():
        result += f'{key} is a {value}\n '
    return result

def combined():
    nums=[2, 4, 6, 8]
    for x in nums:
        for all in 'abc':
            return(x, all)

def find_the_number():
    x = 0
    while True:
        if x == 78:
            print("found 15436!")
            break
        else:
            x+=1

def find_the_email_address():
    sentence = "Dave gave me his email, which was dave_402@gmail.com"
    email = re.findall("\S+@\S+.com", sentence)
    return email

def suitcase_charge():
    suitcase_weight = float(input("Enter your suitcase weight (in lbs): "))
    if suitcase_weight > 50:
        return("You will have to pay a $50 overweight fee")
    else:
        return("You are good to go! Have a safe flight")

def random_password_generator():
    length = int(input("enter length of password: "))
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return ("The randomly generated password is: %s" % result_str)

def pop_function():
    list = ["chicken", "pig", "cow", "duck", "turkey", "goat", "sheep"]
    pop_item = list.pop(2)
    return (pop_item, "was taken out, the new list now is: ", list)
