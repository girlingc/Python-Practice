
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

def display_all(input_dict):
    for province, capital in input_dict.items():
            print(capital, 'is the capital city of', province)
            print("")
    return input_dict


def get_capital_city(province_name, input_dict):
    check = province_name
    for (province, capital) in input_dict.items():
        if province == check:
            print("The capital of", check, "is:", capital)
            print("")
            return capital


def add_item(province_name, capital_city, input_dict):
    old_number = len(input_dict)
    add_province = province_name
    add_capital = capital_city
    input_dict[add_province] = add_capital
    print("Before", old_number, "elements, after", len(input_dict))
    return province_name, capital_city


def remove_item(province_name, input_dict):
    old_number = len(input_dict)
    remove_province = province_name
    input_dict.pop(remove_province, None)
    print("Before", old_number, "elements, after", len(input_dict))
    return province_name