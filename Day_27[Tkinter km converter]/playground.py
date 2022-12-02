def add(*args):
    i =0
    for n in args:
        i = i +n
    print(i)


add(4,9,8,5)


class Car():
    def __init__ (self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.seats = kw.get("seats")

my_car=Car(make="nissan",model="GT-8",seats=3)
print(my_car.model)

from tkinter import *

window =Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)
# label
my_label = Label(text="I am a Label", font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

my_label["text"] = "new text"
my_label.config(text="new text")

window.config(padx=20, pady=20)
# label
my_label = Label(text="I am a Label", font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

my_label["text"] = "new text"
my_label.config(text="new text")


def button_clicked():
    new_txt = input.get()
    my_label.config(text=new_txt)


button = Button(text="click me", command=button_clicked)
button.grid(column=1,row=1)
inp = Entry(width=10)
inp.grid(column=3,row=2)

new_button = Button(text="New Button")
new_button.grid(row=0,column=2)
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
