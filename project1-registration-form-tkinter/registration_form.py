from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Counter to keep track of the number of forms submitted
form_counter = 0

# List of valid emails (simulated database)
valid_emails = ['user1@example.com', 'user2@example.com', 'user3@example.com']

def submit_form():
    # Add your logic to handle form submission here
    full_name = enter_1.get()
    email = enter_3.get()
    attendance_type = attendance_var.get()
    language = language_var.get()
    country = country_var.get()
    gender = gender_var.get()
    meeting_date = datetime.now().strftime("%Y-%m-%d")
    
    # Check if Full Name, Email, Attendance type, Language, Country, and Gender fields are not empty
    if not full_name or not email or not attendance_type or not language or not country or not gender:
        messagebox.showerror("Error", "Please fill all fields.")
        return
    
    # Check if the email is in a valid format
    if '@' not in email or '.' not in email:
        messagebox.showerror("Error", "Please enter a valid email address.")
        return
    
    # Check if the email exists in the list of valid emails
    #if email not in valid_emails:
        #messagebox.showerror("Error", "The entered email does not exist.")
        #return
    
    # If all validation passes, increment the form counter and print a success message
    global form_counter
    form_counter += 1
    print(f"Form submitted! Total forms submitted: {form_counter}")
    print(f"Date: {meeting_date}, Attendance Type: {attendance_type}, Language: {language}, Country: {country}, Gender: {gender}")

def submit_another_form():
    # Reset the form counter to 0 when submitting another form
    global form_counter
    form_counter = 0
    # Add your logic for submitting another form here
    # For now, let's just clear the entry fields
    enter_1.delete(0, END)
    enter_3.delete(0, END)
    attendance_var.set(0)
    language_var.set('')
    country_var.set('')
    gender_var.set('')
    print("Another form submitted! Total forms submitted: 0")

def exit_application():
    base.destroy()

# Creating the object 'base' of the Tk()
base = Tk()

# Using the Geometry method to set certain dimensions
base.geometry("550x600")

# Using title method to give the title to the window
base.title('Registration form')

# Using 'Label' method to add widget in the Registration Form and also use place() method to set their positions.
lbl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
lbl_0.place(x=90, y=60)

# Using 'Label' widget to create Full name label and using place() method to set its position.
lbl_1 = Label(base, text="FullName", width=20, font=("bold", 10))
lbl_1.place(x=80, y=130)

# Using Entry widget to make a text entry box for accepting the input string in text from the user.
enter_1 = Entry(base)
enter_1.place(x=240, y=130)

# Using 'Label' widget to create Email label and using place() method to set its position.
lbl_3 = Label(base, text="Email", width=20, font=("bold", 10))
lbl_3.place(x=68, y=180)

# Using Entry widget to make a text entry box for accepting the input string in text from the user.
enter_3 = Entry(base)
enter_3.place(x=240, y=180)

# Using 'Label' widget to create Attendance type label and using place() method to set its position.
lbl_attendance = Label(base, text="Attendance Type", width=20, font=("bold", 10))
lbl_attendance.place(x=50, y=230)

# Using variable 'attendance_var' to store the integer value, which by default is 0
attendance_var = StringVar()

# Using Radio button widget to create an option choosing button and using place() method to set its position.
Radiobutton(base, text="Physical", padx=5, variable=attendance_var, value="Physical").place(x=240, y=230)
Radiobutton(base, text="Online", padx=20, variable=attendance_var, value="Online").place(x=320, y=230)

# Using 'Label' widget to create Language label and using place() method to set its position.
lbl_language = Label(base, text="Language", width=20, font=("bold", 10))
lbl_language.place(x=50, y=280)

# This creates a list of languages available in the dropdown list.
list_of_languages = ['English', 'Spanish', 'French', 'German']

# The variable 'language_var' is introduced to store the String Value, which by default is (empty) ""
language_var = StringVar()
language_var.set('Select your Language')
language_dropdown = OptionMenu(base, language_var, *list_of_languages)
language_dropdown.config(width=15)
language_dropdown.place(x=240, y=280)

# Using 'Label' widget to create Countries label and using place() method to set its position.
lbl_country = Label(base, text="Country", width=20, font=("bold", 10))
lbl_country.place(x=50, y=330)

# This creates a list of countries available in the dropdown list.
list_of_countries = ['India', 'Canada', 'US', 'Germany', 'UK']

# The variable 'country_var' is introduced to store the String Value, which by default is (empty) ""
country_var = StringVar()
country_var.set('Select your Country')
country_dropdown = OptionMenu(base, country_var, *list_of_countries)
country_dropdown.config(width=15)
country_dropdown.place(x=240, y=330)

# Using 'Label' widget to create Gender label and using place() method to set its position.
lbl_gender = Label(base, text="Gender", width=20, font=("bold", 10))
lbl_gender.place(x=50, y=380)

# The new variable 'gender_var' is created to store Integer Value, which by default is 0.
gender_var = StringVar()

# Using Radio button widget to create an option choosing button and using place() method to set its position.
Radiobutton(base, text="Male", padx=5, variable=gender_var, value="Male").place(x=240, y=380)
Radiobutton(base, text="Female", padx=20, variable=gender_var, value="Female").place(x=320, y=380)

# Using the Button widget, we get to create a button for submitting all the data that has been entered in the entry boxes of the form by the user.
Button(base, text='Submit', width=20, bg="black", fg='white', command=submit_form).place(x=180, y=430)

# Adding a button to submit another form
Button(base, text='Submit Another Form', width=20, command=submit_another_form).place(x=180, y=470)

# Adding a button to exit the application
Button(base, text='Exit', width=20, command=exit_application).place(x=180, y=510)

# Calling the mainloop method to execute the entire program
base.mainloop()
