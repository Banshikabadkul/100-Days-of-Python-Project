from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=400,height=200)
window.config(padx=20, pady=20)

# entry

inp = Entry(width=10)
inp.grid(row=0,column=1)


# label1

label_mile = Label(text="Miles",font=("Arial",15))
label_mile.grid(row=0,column=2)
label_mile.config(padx=10,pady=10)

# label2.1
label_equal = Label(text="is equal to",font=("Arial",15))
label_equal.grid(row=1,column=0)
label_equal.config(padx=10,pady=10)

# label2.2
label_inp = Label(text="0",font=("Arial",15))
label_inp.grid(row=1,column=1)
label_inp.config(padx=10,pady=10)

# label2.3
label_km = Label(text="Km",font=("Arial",15))
label_km.grid(row=1,column=2)
label_km.config(padx=10,pady=10)

# button


def mile_to_km():
    miles = float(inp.get())
    kilometres = miles * 1.609344
    label_inp.config(text=f"{kilometres}")



button = Button(text="Calculate",command=mile_to_km)
button.grid(row=2,column=1)
button.config(padx=10,pady=10)
window.mainloop()
