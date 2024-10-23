from tkinter import *

FONT_NAME = "Ariel"

BACKGROUND_COLOR = "#B1DDC6"

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
canvas.create_image(400, 260, image=card_front_img)
title_text = canvas.create_text(
    400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold")
)
canvas.grid(row=0, column=0)


window.mainloop()
