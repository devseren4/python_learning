from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import string

FONT_NAME = "Roboto"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def button_add():

    website = web_box.get()
    email = info_box.get()
    password = password_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        try:
            with open("data.json", "r") as save_file:
                # reading old data
                data = json.load(save_file)
        except FileNotFoundError:
            with open("data.json", "w") as save_file:
                json.dump(new_data, save_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as save_file:
                # saving update data
                json.dump(data, save_file, indent=4)
        finally:
            web_box.delete(0, END)
            password_box.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = web_box.get()
    try:
        with open("data.json") as save_file:
            data = json.load(save_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}"
            )
        else:
            messagebox.showinfo(
                title="Error", message=f"No details for {website} exists."
            )


# ---------------------------- UI SETUP ------------------------------- #
# CREATE THE WINDOW
window = Tk()
window.config(padx=50, pady=50)
window.title("Pasword Manager")

# CREATE THE CANVAS
canvas = Canvas(
    width=200,
    height=200,
)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS
web_label = Label(text="Website:", font=(FONT_NAME, 10, "normal"))
web_label.grid(row=1, column=0)

info_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "normal"))
info_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=(FONT_NAME, 10, "normal"))
password_label.grid(row=3, column=0)

# ENTRY
web_box = Entry(width=35)
web_box.grid(row=1, column=1, sticky="EW")
web_box.focus()

info_box = Entry(width=35)
info_box.grid(row=2, column=1, columnspan=2, sticky="EW")
info_box.insert(0, "serenastoica3@gmail.com")

password_box = Entry(width=21)
password_box.grid(row=3, column=1, sticky="EW")

# BUTTONS
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW", padx=10)

add_button = Button(text="Add", width=36, command=button_add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW", padx=10)
window.mainloop()
