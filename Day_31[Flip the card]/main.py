BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

curr_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"],fill="white")
    canvas.itemconfig(canvas_img, image=new_img)


def next_card():
    global curr_card
    global flip_timer
    windows.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    french = curr_card["French"]
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=french,fill="black")
    canvas.itemconfig(canvas_img,image=old_img)
    flip_timer = windows.after(3000, func=flip_card)

def is_known():
    to_learn.remove(curr_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

windows = Tk()
windows.title("Flashy")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)


canvas = Canvas(width=800,height=526)
old_img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400,263,image=old_img)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="",fill="black",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",fill="black",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2 )

cross_image = PhotoImage(file="images/wrong.png")
button = Button(image=cross_image, highlightthickness=0,command=next_card)
button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
button_2 = Button(image=check_image, highlightthickness=0,command=is_known)
button_2.grid(row=1,column=1)
next_card()


windows.mainloop()



