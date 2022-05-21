import re
import tkinter as tk
def interface():
    root = tk.Tk()
    root.title("Lab 9")

    canvas1 = tk.Canvas(root, width = 400, height = 300, relief = 'raised')
    canvas1.pack()

    label1 = tk.Label(root, text="Validation")
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)

    label3 = tk.Label(root, text='Type your Entry:')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(200, 100, window=label3)

    entry1 = tk.Entry(root, width=50)
    canvas1.create_window(200, 140, window=entry1)

    def isValidLicensePlate():

        license_plate = entry1.get() 
        if re.match("[A-Z]{2}[0-9]{1}-[0-9]{2}[A-Z]{1}$", license_plate):
            label2 = tk.Label(root, text="This is a valid BC license plate", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True
        elif re.match("[A-Z]{3}[0-9]{3}$", license_plate):
            label2 = tk.Label(root, text="This is a valid BC license plate", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True
        elif re.match("[A-Z]{3} [0-9]{3}$", license_plate):
            label2 = tk.Label(root, text="This is a valid BC license plate", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True
        elif re.match("[0-9]{3}[A-Z]{3}$", license_plate):
            label2 = tk.Label(root, text="This is a valid BC license plate", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True
        elif re.match("[A-Z]{2}[0-9]{1} {1}[0-9]{2}[A-Z]{1}$", license_plate):
            label2 = tk.Label(root, text="This is a valid BC license plate", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True

        else:
            label2 = tk.Label(root, text="This is not a valid BC license plate", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return False

    def isValidPythonVariableName():

        variable_name = entry1.get()
        if re.match("(?!.*__)[_a-z]", variable_name):
            label2 = tk.Label(root, text="This is a valid Python variable name", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True

        else:
            label2 = tk.Label(root, text="This is not a valid Python variable name", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return False


    def isValidEmailAddress():
        email = entry1.get()

        email_data = re.split("@", str(email))
        username = email_data[0]
        domain_data = re.split("[.]", email_data[1])
        domain_name = domain_data[0]
        top_level_domain = domain_data[1]

        if re.match("(?!.*_$)(?!.*_^)(?!.*_$)[A-Za-z_]", str(username)) and re.match("[a-zA-Z]", str(domain_name)) and re.match("[a-zA-Z]", str(top_level_domain)):
            label2 = tk.Label(root, text="This is a valid Email Address", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            print(username, domain_name, top_level_domain)
            return True
        else:
            label2 = tk.Label(root, text="This is not a valid Email Address", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            print(email)
            print(username)
            print(domain_name)
            print(top_level_domain)
            return False


    def isValidHumanHeight():

        height = entry1.get()

        if re.match('''[2-8]{1}'{1}[0-9]{1}"{1}''', height):
            label2 = tk.Label(root, text="This is a valid Human Height", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return True
        else:
            label2 = tk.Label(root, text="This is a valid Human Height", font=("helvetica", 10, 'bold'))
            canvas1.create_window(200, 120, window=label2)
            return False



    button1 = tk.Button(text="Validate BC License Plate", command=isValidLicensePlate)
    button2 = tk.Button(text = "Validate Python Variable Name", command=isValidPythonVariableName)
    button3 = tk.Button(text="Validate Email Address", command=isValidEmailAddress)
    button4 = tk.Button(text="Validate Human Height", command=isValidHumanHeight)
    button1.config(font=('helvetica', 10))
    button2.config(font=('helvetica', 10))
    button3.config(font=('helvetica', 10))
    button4.config(font=('helvetica', 10))
    canvas1.create_window(200, 180, window=button1)
    canvas1.create_window(200, 210, window=button2)
    canvas1.create_window(200, 240, window=button3)
    canvas1.create_window(200, 270, window=button4)

    root.mainloop()
    
def main():
    interface()
if __name__ == "__main__":
    main()