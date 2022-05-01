countries = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "CÃ´te d'Ivoire (Ivory Coast)", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini (Swaziland)', 'Ethiopia', 'Federated States of Micronesia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia (Macedonia)', 'Northern Ireland', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia', 'Zimbabwe')

def create_list_planets():
    #Hardcode Planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    return planets


def create_file(file_name, items):
    print(items)
    # Write file
    with open(file_name, "w") as f:
        for item in items:
            f.write(item)
            f.write("\n")


def overwrite_file(file_name, text_to_save):
    # Overwrite file
    with open(file_name, "w") as f:
        f.write(f'{text_to_save}\n')
    return text_to_save


def append_to_file(file_name, text_to_append):
    with open(file_name, 'a') as f:
        f.write(f'{text_to_append}\n')


def sort_planets(in_file, out_file):
    planets = []
    with open(in_file, 'r') as f:
        for line in f:
            planets.append(line.split("\n")[0])
    planets.sort()
    create_file(out_file, planets)
    return 


def filter_countries(input_list, string_to_filter):
    create_file('Countries.txt', countries)
    with open('Countries.txt', 'r') as in_file:
        with open('FilteredCountries', 'w') as out_file:
            for line in in_file:
                line = line.split('\n')[0]
                if string_to_filter in line:
                    out_file.write(f'{line}\n')






def print_dashboard():
    # Printing the user interface
    print("""
    ==============================
    Choose 1-4 or 0 to exit
    ------------------------------
    [1] Read file
    [2] Create or Write in file
    [3] Overwrite in file
    [4] Append to file
    [5] Sort planets
    [6] Filter Countries
    [0] Exit
    ==============================
    """)

    # Obtaining what function the user wants to input
    user_selection = input("What function do you want to choose? ")
    
    if user_selection == "1":
        create_list_planets()
        return True

    elif user_selection == "2":
        create_file('Planets.txt', create_list_planets())
        return True

    elif user_selection == "3":
        overwrite = str(input("What do you want to write in the file? "))
        print(overwrite_file('Planets.txt', overwrite))
        return True
    
    elif user_selection == "4":
        append = str(input("What would you like to add? "))
        append_to_file('Planets.txt', append)
        return True

    elif user_selection == "5":
        sort_planets('Planets.txt', 'PlanetsSorted.txt')
        return True
    
    elif user_selection == "6":
        filter_countries(countries, 'an')
        return True

    elif user_selection == "0":
        print("Thank you for using my program :)")
        return False
    
    else:
        print("Please choose either [1], [2], [3], [4], or [0]")
        return True


def main():
    program_running = True

    while program_running:
        program_running = print_dashboard()



if __name__ == "__main__":
    main()