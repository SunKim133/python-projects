from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_pwd.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    new_password = "".join(password_list)

    input_pwd.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get().title()
    try:
        with open('data.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(message=website, detail=f"Email: {email}\nPassword:{password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(message="No details for the website exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get().title()
    email = input_email.get()
    password = input_pwd.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or password == "":
        messagebox.showinfo(message='Oops!', detail="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(message=website, detail=f"These are the details entered:\nEmail/Username: {email}\nPassword: {password}\nIs it okay to save?")

    if is_ok:
        try:
            with open('data.json', mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_pwd.delete(0, END)
            input_website.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label - 'Website'
label_website = Label(text='Website: ')
label_website.grid(column=0, row=1, sticky=E)

# Label - 'Email/Username'
label_email = Label(text='Email / Username: ')
label_email.grid(column=0, row=2, sticky=E)

# Label - 'Password'
label_pwd = Label(text='Password: ')
label_pwd.grid(column=0, row=3, sticky=E)

# Button-Generate
btn_generate = Button(text='Generate', width=5, command=generate_password)
btn_generate.grid(column=2, row=3)

# Button-Add
btn_add = Button(text='Add', width=28, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

# Button-Search
btn_add = Button(text='Search', width=5, comman=find_password)
btn_add.grid(column=2, row=1)

# Entry-Website
input_website = Entry(width=21)
input_website.grid(column=1, row=1)
input_website.focus()

# Entry-Email
input_email = Entry(width=30)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, 'sample@gmail.com')

# Entry-Password
input_pwd = Entry(width=21)
input_pwd.grid(column=1, row=3)


window.mainloop()