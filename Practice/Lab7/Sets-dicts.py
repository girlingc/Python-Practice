import utilities_sets, utilities_dict
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

def main():

    dict_prov_teritories = dict(Ontario='Toronto', Quebec='Quebec City', Nova_Scotia='Halifax', New_Brunswick='Fredericton', Manitoba='Winnipeg', British_Columbia='Victoria', Prince_Edward_Island='Charlottetown', Saskatchewan='Regina', Alberta='Edmonton', Newfoundland_and_Labrador="St. John's")
    my_set1 = {"apple", "banana", "orange", "peach"}
    my_set2 = {"banana", "pineapple", "peach", "watermelon"}
    

    print("""
    ==============================
    Choose 1-2 or 0 to exit
    ------------------------------
    [1] Part A - Sets
    [2] Part B - Dictionaries
    [0] Exit
    ==============================
    """)

    module_selection = get_typed_input("What module would you like to choose?", 'int')

    if module_selection == 1:
        print("""
        ==============================
        Choose 1-5 or 0 to exit
        ------------------------------
        [1] List number of elements
        [2] List elements
        [3] Add elements
        [4] Remove elements
        [5] Get union
        [0] Exit
        ==============================
        """)

        # Obtaining what function the user wants to input
        user_selection = get_typed_input("What function do you want to choose? ", 'str')
        
        if user_selection == "1":
            chosen_set = get_typed_input("What set would you like to choose? ", 'str')
            if chosen_set == "1":
                utilities_sets.get_total_items(my_set1)
                return True
            elif chosen_set == "2":
                utilities_sets.get_total_items(my_set2)
                return True
            else:
                print("Please enter either 1 or 2")

        elif user_selection == "2":
            chosen_set = get_typed_input("What set would you like to choose? ", "str")
            if chosen_set == "1":
                utilities_sets.display_all_items(my_set1)
                return True
            elif chosen_set == "2":
                utilities_sets.display_all_items(my_set2)
                return True
            else:
                print("Please enter either 1 or 2")

        elif user_selection == "3":
            chosen_set = get_typed_input("What set would you like to choose? ", "str")
            if chosen_set == "1":
                utilities_sets.add_item(get_typed_input("What would you like to add? ", 'str'), my_set1)
                return True
            elif chosen_set == "2":
                utilities_sets.add_item(get_typed_input("What would you like to add? ", 'str'), my_set2)
                return True
            else:
                print("Please enter either 1 or 2")
        
        elif user_selection == "4":
            chosen_set = get_typed_input("What set would you like to choose? ", "str")
            if chosen_set == "1":
                utilities_sets.remove_item(get_typed_input("What would you like to remove? ", 'str'), my_set1)
                return True
            elif chosen_set == "2":
                utilities_sets.remove_item(get_typed_input("What would you like to remove? ", 'str'), my_set2)
                return True
            else:
                print("Please enter either 1 or 2")

        elif user_selection == "5":
            utilities_sets.get_the_union_of(my_set1, my_set2)
            return True

        elif user_selection == "0":
            print("Thank you for using my program :)")
            return False
        
        else:
            print("Please choose either [1], [2], [3], [4], [5] or [0]")
            return True

    elif module_selection == 2:
        # Printing the user interface
        print("""
        ==============================
        Choose 1-4 or 0 to exit
        ------------------------------
        [1] List capital cities of provinces
        [2] Get capital city
        [3] Add elements
        [4] Remove elements
        [0] Exit
        ==============================
        """)

        # Obtaining what function the user wants to input
        user_selection = get_typed_input("What function do you want to choose? ", 'str')

        if user_selection == "1":
            utilities_dict.display_all(dict_prov_teritories)
            return True

        elif user_selection == "2":
            utilities_dict.get_capital_city(get_typed_input("What province do you want to know the capital of? ", 'str'), dict_prov_teritories)
            return True

        elif user_selection == "3":
            utilities_dict.add_item(get_typed_input("Enter the province you would like to add: ", 'str'), get_typed_input("Enter the province's capital city: ", 'str'), dict_prov_teritories)
            return True
        
        elif user_selection == "4":
            utilities_dict.remove_item(get_typed_input('Enter the province you would like to remove: ', 'str'), dict_prov_teritories)
            return True


        elif user_selection == "0":
            print("Thank you for using my program :)")
            return False
            
        else:
            print("Please choose either [1], [2], [3], [4], or [0]")
            return True


    elif module_selection == 0:
        print("Thank you for using my program :)")
        return False

    else:
        print("Please choose either [1], [2] or [0]")
        


if __name__ == "__main__":
    main()