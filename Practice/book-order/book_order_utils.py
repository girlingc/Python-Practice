import os
import re

def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):

    try:
        int(order_num) > 0
    except:
        raise ValueError("Order Number is invalid")


    if len(title) < 0 or not re.match("^[a-zA-Z\s]+$", title):
        raise ValueError("Title is invalid")


    if len(author) < 0 or re.match("^[a-zA-Z\s']+$ ", author):
        raise ValueError("Author is invalid")


    try:
        int(isbn)
    except:
        raise TypeError("ISBN must be an integer")

    if len(isbn) > 20 or (len(isbn) < 4):
        raise ValueError("ISBN is invalid")



    try:
        int(year)
    except:
        raise TypeError("Year must be an integer")

    if len(year) != 4:
        raise ValueError("Year is invalid")



    try:
        int(quantity)
    except:
        raise TypeError("Quantity must be an integer")
    if 1000 < int(quantity) or int(quantity) < 0:
        raise ValueError("Quantity is invalid")



    try:
        float(cost)
    except:
        raise ValueError("Cost is invalid")
    if float("{0:.2f}".format(float(cost))) != float(cost):
        raise ValueError("Cost is invalid")



def calculate_per_book_cost(cost, quantity):
    try:
        total_cost = (float(cost)/float(quantity))
    except:
        raise ZeroDivisionError("float division by zero")
    return float(total_cost)





def write_book_order_details(filename):
    with open("test.txt", "w") as f:
        f.writelines(["Book Order", "title = 'Intro to Python'", "author = 'Bill Smith'", "isbn = '123456'", "year = '2010'", "quantity = '10'", "cost = '500.50'", "unit_cost = '50.05'"])


        if os.path.isfile(filename):
            raise ValueError("Order file name already exists!")
        else:
            "File does not exist"
