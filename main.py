from tkinter import *
from tkinter import messagebox
import json
from random import randint, choice, shuffle

import pyperclip as pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    website_for_search = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(message="no data found!")
    else:
        if website_for_search in data:
            email = data[website_for_search]["email"]
            password = data[website_for_search]["password"]
            messagebox.showinfo(message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(message=f"no password found for {website_for_search}!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": username,
        "password": password
    }

    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror("ops", "please fill all fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password generator")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Entries
website_input = Entry(width=18)
website_input.grid(column=1, row=1)
website_input.focus()
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "@gmail.com")
password_input = Entry(width=18)
password_input.grid(column=1, row=3)
# Buttons
add_button = Button(text="add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

window.mainloop()
