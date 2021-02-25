import tkinter
from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

answers = ["America", "India", "Australia"]

questions = []

for i in answers:
    words = list(i)
    shuffle(words)
    questions.append(words)

num = random.randint(0, len(questions) - 1)

def initial():
    global questions, num
    lb1.configure(text=questions[num])

def answercheck():
    global questions,num, answers
    userinput = e1.get()
    if userinput == answers[num]:
        messagebox.showinfo("success","Your answer is correct")
    else:
        messagebox.showinfo("Error", "Incorrect answer")
        e1.delete(0, END)

def resetswitch():
    global questions,num, answers
    num= random.randint(0, len(questions)- 1)
    lb1.configure(text=questions[num])
    e1.delete(0, END)

window = Tk()
window.geometry=("300x300")
window.configure(background='#5DA3FA')
window.title("Jumblebot")


lb1 = Label(window, font='times 20', bg='#5DA3FA', fg='#0D0D0D')
lb1.pack(pady=30, ipady=10, ipadx=10)

answer = StringVar()
e1 = Entry(window, textvariable=answer)
e1.pack(ipady=5, ipadx=5)

button1 = Button(window, text="Check",bg='#E8BD0D', width=20, command= answercheck)
button1.pack(pady=40)

button2 = Button(window, text="Reset",bg='#E8BD0D', width=20, command=resetswitch)
button2.pack(pady=40)





initial()
window.mainloop()