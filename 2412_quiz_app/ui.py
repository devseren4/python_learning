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
            width=280,
            text="Some question",
            fill=THEME_COLOR,
            font=(FONT_NAME, 20, "italic"),
        )
        self.canva.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_button_img, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_button_img,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text, text=q_text)
        else:
            self.canva.itemconfig(
                self.question_text, text="You've reached the end of the quiz"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.get_next_question)
