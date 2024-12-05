from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Ariel"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canva = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canva.create_text(
            150,
            125,
            text="Some question",
            fill=THEME_COLOR,
            font=(FONT_NAME, 20, "italic"),
        )
        self.canva.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_button_img,
            highlightthickness=0,
        )
        self.true_button.grid(row=2, column=0)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canva.itemconfig(self.question_text, text=q_text)
