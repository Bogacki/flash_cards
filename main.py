import random
from tkinter import *
from random import choice
from time import sleep

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ------------------- FUNCTIONS
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(flash_card_language,text="English", fill="black")
    flash_card.itemconfig(flash_card_word,text=current_card["English"], fill="black")
    flash_card.itemconfig(flash_card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(flash_card_image, image=card_back)
    flash_card.itemconfig(flash_card_language,text="Polski", fill="white")
    flash_card.itemconfig(flash_card_word,text=current_card["Polish"], fill="white")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)

    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# ---------------- WINDOW CONFIG
window = Tk()
window.title("Flashy Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False,False)
w = 900
h = 726

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

flip_timer = window.after(3000, func=flip_card)

# ------------------ CARDS CONFIG

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")



flash_card = Canvas(width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_image = flash_card.create_image(400,263,image=card_front)
flash_card.grid(column=1, row=1, columnspan=2)
flash_card_language = flash_card.create_text(400,150,text="",font=("Ariel",40,"italic"))
flash_card_word = flash_card.create_text(400,263,text="",font=("Ariel",60,"bold"))


wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=1,row=2)


right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=2,row=2)

next_card()


























window.mainloop()