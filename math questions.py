#math questions
from tkinter import * #this imports tkinter into the code (tkinter is used to make GUI)
from random import *
from time import *


def next_question():

    global i
    global x
    global y
    
    x = randrange(10)
    y = randrange(10)    
    
    question_text = str(x) + " + " + str(y) + " = "
    problem_label.configure(text = question_text)
    ans_entry.delete(0, END)
    ans_entry.focus()
    
    lbl_question = Label(root, width = 10, padx = 40, pady = 10, font = ("Times", "15", "bold italic"), text = "Question " + str(i))
    lbl_question.grid(row=0, column=0)
    i = i+1


def check_answer():
    
    answer = x + y
    
    try:
        user_answer = int(ans_entry.get())
        
        if user_answer == answer:
            feedback.configure(text = "Correct!")
        elif user_answer == "":
            feedback.configure(text = "Please answer the question")
        else:
            feedback.configure(text = "Wrong!")
            ans_entry.delete(0, END)
            next_question()
        
    except ValueError:
        feedback.configure(text = "That is not a number!")
        ans_entry.delete(0, END)
        ans_entry.focus()

#main loop

i = 1

root = Tk()
root.title("MathQuiz")

x = randrange(10)
y = randrange(10)

feedback = Label(root, text = "", height = 3)
feedback.grid(row=5, column=0)

question_label = Label(root, width = 10, padx = 40, pady = 10, font = ("Times", "15", "bold italic"))
question_label.grid(row=0, column = 0)

problem_label = Label(root, width = 10, padx = 40, pady = 10, text = "", font = ("Times", "15", "bold italic"))
problem_label.grid(row=1, column=0, sticky = W)

ans_entry = Entry(root, width=15)
ans_entry.grid(row=2, column=0)

check_btn = Button(root, text = "Check your answer", command = check_answer, relief = RIDGE)
check_btn.grid(row=3, column=0)

next_btn = Button(root, text = "Next", command = next_question, relief = RIDGE)
next_btn.grid(row=4, column=0)


root.geometry("200x200+850+0")
next_question()
root.mainloop()