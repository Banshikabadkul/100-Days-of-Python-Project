# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
import pyperclip

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    e_3.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200,highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

# label1
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

# label2
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# label3
pas_label = Label(text="Password:")
pas_label.grid(row=3, column=0)



# entry1
e_1 = Entry(width=35)
e_1.grid(row=1, column=1, columnspan=2)
e_1.focus()

# entry2
e_2 = Entry(width=35)
e_2.grid(row=2, column=1, columnspan=2)
e_2.insert(0,"angela@gmail.com")
# entry3
e_3 = Entry(width=21)
e_3.grid(row=3,column=1)

# label4
gen_label = Button(text="Generate Password",command=gen_pass)
gen_label.grid(row=3, column=2)


def data_save():
    web = e_1.get()
    email = e_2.get()
    passw = e_3.get()
    if len(web)==0 or len(passw)==0:
        messagebox.showinfo(title="oops",message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web,
                                       message=f"These are the detailed entered:\n Email: {email}\n Password:{passw}\n Is it ok to save")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{web}| {email}| {passw}\n ")
                e_1.delete(0, END)
                e_3.delete(0, END)



button = Button(text="Add",width=36,command=data_save)
button.grid(row=4, column=1,columnspan=2)



window.mainloop()