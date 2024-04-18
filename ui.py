from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.true_image = PhotoImage(file="D:/Python Course/Day-34/images/true.png")
        self.false_image = PhotoImage(file="D:/Python Course/Day-34/images/false.png")

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Question will be here",
                                                   font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_incorrect = self.quiz.check_answer("False")
        self.give_feedback(is_incorrect)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
