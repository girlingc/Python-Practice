import csv

def get_book_info_title_author_date(book):
    # This function returns the title of the book, its author, and date published, and will be used in every function
    return book[0] + ' by ' + book[1] + ' (' + book[3].strip() + ')'


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


def year_range():
    # Creating a list and acquiring the search criteria (A start year and an ending year)
    book_list = []
    start_year = get_typed_input("Enter beginning year of search: ", 'int')
    end_year = get_typed_input("Enter end year of search: ", 'int')

    # Finding books that were bestsellers between start and end years and appending them to the list
    with open('bestsellers.txt', 'r') as bs:
        bs_reader = csv.reader(bs, delimiter = '\t')
        for book in bs_reader:
            date = (book[3])
            year = int(date[-4:])
            if year <= end_year and year >= start_year:
                book_list.append(book)

    # Printing if number of titles in list is equal to 0
    if book_list == []:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There were no bestsellers listed between", start_year, "and", end_year)
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
    # Printing list of titles, as well as their respective authors and dates published
    else:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There were", len(book_list), "bestsellers between", start_year, "and", end_year)
        print("")
        print('\n'.join(map(get_book_info_title_author_date, book_list)))
        print('')
        print('-----------------------------------------------------------------------------------')


def specific_month_year():
    # Creating a list and acquiring the search criteria (Specific month and year)
    book_list = []
    choose_month = get_typed_input("Select month (as a number, 1-12): ", 'int')
    choose_year = get_typed_input("Select year: ", 'int')

    # Searching through the bestsellers file and appending books that match the search criteria
    with open('bestsellers.txt', newline = '') as bs:
        bs_reader = csv.reader(bs, delimiter = '\t')
        for book in bs_reader:
            dates = (book[3]).split('/')
            year = int(dates[2])
            month = int(dates[0])
            if choose_year == year and choose_month == month:
                book_list.append(book)

    # Printing if number of titles in list is equal to 0
    if book_list == []:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There were no bestsellers on the", choose_month, "month of", choose_year)
        print('')
        print('-----------------------------------------------------------------------------------')

    # Printing list of titles, as well as their respective authors and dates published
    else:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("The", len(book_list), "bestsellers in", choose_month, "of", choose_year, "were:")
        print('\n'.join(map(get_book_info_title_author_date, book_list)))
        print('')
        print('-----------------------------------------------------------------------------------')


def search_for_author():
    # Creating a list and acquiring the search criteria (String to search through the authors)
    author = []
    input_filter = get_typed_input('Input a string to filter authors: ', 'str').lower()

    # Searching through the bestsellers file and appending books that match the criteria
    with open('bestsellers.txt', newline = '') as bs:
        bs_reader = csv.reader(bs, delimiter = '\t')
        for book in bs_reader:
            if input_filter in book[1].lower():
                author.append(book)

    # Printing if number of titles in list is equal to 0
    if author == []:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are no authors with", input_filter, "in their name.")
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
    # Printing list of titles, as well as their respective authors and dates published
    else:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are", len(author), "books by an author with", input_filter, "in their name:")
        print('')
        print('\n'.join(map(get_book_info_title_author_date, author)))
        print('')
        print('-----------------------------------------------------------------------------------')


def search_for_title():
    # Creating a list and acquiring the search criteria (String to search through the book authors)
    title = []
    input_filter = get_typed_input(('Input a string to filter book titles :'), 'str').lower()

    # Searching through the bestsellers file and appending books that match the criteria
    with open('bestsellers.txt', newline = '') as bs:
        bs_reader = csv.reader(bs, delimiter = '\t')
        for book in bs_reader:
            if input_filter in book[0].lower():
                title.append(book)

    # Printing if number of titles in list is equal to 0
    if title == []:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are no bestsellers with", input_filter, "in their name.")
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
    # Printing list of titles, as well as their respective authors and dates published
    else:
        print('')
        print('-----------------------------------------------------------------------------------')
        print('')
        print("There are", len(title), "books with", input_filter, "in their title:")
        print("")
        print('\n'.join(map(get_book_info_title_author_date, title)))
        print('')
        print('-----------------------------------------------------------------------------------')


def print_dashboard():
    # Printing the user interface
    print("""
    Please choose an option
    1: Look up year range
    2: Look up month/year
    3: Search for author
    4: Search for title
    
    Q: Quit
    """)


    # Obtaining what function the user wants to input
    user_selection = input(" ")
    
    if user_selection == "1":
        year_range()
        return True

    elif user_selection == "2":
        specific_month_year()
        return True

    elif user_selection == "3":
        search_for_author()
        return True
    
    elif user_selection == "4":
        search_for_title()
        return True


    elif user_selection == "q" or user_selection == "Q":
        print("Thank you for using my program :)")
        return False
    
    else:
        print("Please choose either 1, 2, 3, 4 or Q to quit")
        return True


def main():
    program_running = True

    while program_running:
        program_running = print_dashboard()


if __name__ == "__main__":
    main()