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


def get_total_items(myset):
    # Returns the total number of items for the given set ("Number of elements = X")
    print("Number of elements in Set 2 =", len(myset))
    return myset

def display_all_items(my_set):
    # Prints all the elements for the given set using iteration (returns list)
    for val in my_set:
        print(val)
    return list(my_set)


def add_item(item, my_set):
    # Adds the given item to the set (Returns list)
    my_set.add(item)
    print("The elements in Set 2 are now:", my_set)
    return list(my_set)


def remove_item(item, my_set):
    # Removes the given item from the set (Returns list)
    my_set.remove(item)
    print("The elements in Set 1 are now:", my_set)
    return list(my_set)


def get_the_union_of(my_set1, my_set2):
#     #returns a set of the union of the given my_set1 and my_set2 (returns the list of the union of the sets)
    union = list(my_set1.union(my_set2))
    print("The union of Set 1 and Set 2 is:", my_set1.union(my_set2))
    return list(union)