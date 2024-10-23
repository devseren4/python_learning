from tkinter import *
import pandas
import random

FONT_NAME = "Ariel"

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = ""


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    window.after(3000, after)


def after():
    global current_card
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------------------- UI ----------------------------------- #

# WINDOW
window = Tk()
window.title("Flash Cards")
window.config(
    bg=BACKGROUND_COLOR,
    padx=50,
    pady=50,
)

# CARD_FRONT
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(
    400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold")
)
canvas.grid(row=0, column=0, columnspan=2)

# WRONG BUTTON
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# RIGHT BUTTON
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()


window.mainloop()
