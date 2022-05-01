import os, csv
def get_typed_input(prompt = "Enter Value", return_type = "str"):
    # Checking for invalid inputs
    try:
        return eval(return_type)(input(prompt))
    except ValueError:
        print("Oops, please enter a", return_type)
        return get_typed_input(prompt, return_type)

def get_car_info():
    make = get_typed_input("What make is the car?", 'str')
    model = get_typed_input("What model is the car?", 'str')
    year = get_typed_input("What year is the car?", 'int')
    license_plate = get_typed_input("What is the license plate?", 'str')
    car_info = f'{make}/{model}/{year}/{license_plate}' 
    return car_info

def convert_to_json_format(car_info):
    car_fields = ["", "", "", ""]
    car_values = car_info.split("/")
    json_format = "{"
    for index,field in enumerate(car_fields):
        json_format +=f'"{field}":"{car_values[index]}"'
        if index != len(car_fields) - 1:
            json_format += ","
    json_format += "}"
    return json_format

def write_parking_file(json_format):
    if os.path.isfile("cars.txt"):
        with open("cars.txt", "a") as cars:
            cars.write(json_format +'\n')
    else:
        with open("cars.txt", "w") as cars:
            cars.write(json_format + '\n')

def list_cars():
    with open("cars.txt", newline = '') as f:
        f_reader = csv.reader(f, delimiter = ',')
        for car in f_reader:
            make = car[0]
            model = car[1]
            year = car[2]
            license_plate = car[3]
            print(year, make, model, "with", license_plate)


def print_dashboard():
    # Printing the user interface
    print("""
    ==============================
    Choose 1-4 or 0 to exit
    ------------------------------
    [1] Add Car
    [2] List Cars
    [3] Find Car
    [0] Exit
    ==============================
    """)

    # Obtaining what function the user wants to input
    user_selection = input("What function do you want to choose? ")
    
    if user_selection == "1":
        car_info = get_car_info()
        json_format = convert_to_json_format(car_info)
        write_parking_file(json_format)
        return True

    elif user_selection == "2":
        list_cars()
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