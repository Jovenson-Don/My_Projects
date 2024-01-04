from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    generated_password = ''.join(password_list)

    shuffle(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    username = username_entry.get().title()
    password = password_entry.get().title()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if website == "" or password == "":
        messagebox.showwarning(title="Error", message="Username or Password has an empty field. "
                                                      "Please go back and correct.")
    else:
        try:
            with open("password.json", "r") as password_file:
                data = json.load(password_file)
        except FileNotFoundError:
            with open("password.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        except ValueError:
            with open("password.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", "w") as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():

    search = website_entry.get().title()
    try:
        with open("password.json") as data:
            data = json.load(data)
            print(data)
        if search in data:
            search_username = data[f"{search}"]['username']
            search_password = data[f"{search}"]['password']
            messagebox.showinfo(title=f"{search}", message=f"Username: {search_username}\nPassword: {search_password}")
        else:
            messagebox.showerror(title="Error", message=f"No results found for {search}.")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No data file found")


# ---------------------------- HIDE/SHOW PASSWORD ------------------------------- #
def check_password():
    print()
    if check_status.get() == 0:
        password_entry.config(show="*")
    else:
        password_entry.config(show="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=29)
website_entry.insert(END, "Facebook")
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=47)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "joeydon21@gmail.com")
check = StringVar()
password_entry = Entry(width=29, show="*", textvariable=check)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(row=4, column=2)
add_button = Button(text="Add", width=24, command=save)
add_button.grid(row=4, column=1)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

# Checkbutton
hide_password = password_entry.get()
check_status = IntVar()
check_button = Checkbutton(text="Show password", variable=check_status, command=check_password)
check_button.grid(row=3, column=2)
window.mainloop()
