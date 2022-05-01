import re
def get_book_info():
    book_title = input("What is the book title? ").strip()
    book_isbn = input("What is the book ISBN? ").strip()
    book_author_last_name = input("What is the book author's last name? ").strip()
    book_publisher = input("Who is the book publisher? ").strip()
    year_published = input("What year was the book published? ").strip()
    book_price = "{:,.2f}".format(float(input("What is the book price? "))).strip()
    book_info = f'{book_title}/{book_isbn}/{book_author_last_name}/{book_publisher}/{year_published}/{book_price}'
    return book_info
    

def convert_to_csv_format(book_info):
    csv_format = re.sub("/", '","', book_info)
    return '"' + csv_format + '"'


def convert_to_json_format(book_info):
    book_fields = ["book_title", "book_isbn", "book_author_last_name", "book_publisher", "year_published", "book_price"]
    book_values = book_info.split("/")
    json_format = "{" 
    for index,field in enumerate(book_fields):
        json_format += f'"{field}":"{book_values[index]}"'
        if index != len(book_fields) - 1:
            json_format += ","

    json_format += "}"
    return json_format


def print_dashboard(book_info):
    print("[1] Convert to CSV format")
    print("[2] Convert to JSON format")
    print("[3] See original book info format")
    print("[0] Exit")


    user_selection = input("What function do you want to choose? ")

    
    if user_selection == "1":
        print(convert_to_csv_format(book_info))
        return True
    
    elif user_selection == "2":
        print(convert_to_json_format(book_info))
        return True

    elif user_selection == "3":
        print(book_info)
        return True

    elif user_selection == "0":
        return False

    else:
        print("Please choose either [1], [2], [3] or [0]")
        return True


def main():
    book_info = get_book_info()
    print(book_info)
    program_running = True

    while program_running:
        program_running = print_dashboard(book_info)

if __name__ == "__main__":
    main()