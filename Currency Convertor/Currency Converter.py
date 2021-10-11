from tkinter import *

window = Tk()

def conversion():
    indianrupees = (float(dollars.get())*75)
    t1.delete("1.0",END)
    t1.insert(END,indianrupees)

    canadian = (float(dollars.get())*1.3)
    t2.delete("1.0",END)
    t2.insert(END,canadian)

    euros = (float(dollars.get())*0.8)
    t3.delete("1.0",END)
    t3.insert(END,euros)

b1 = Button(window, text="Convert", command=conversion)
b1.grid(row=0, column=0)

dollars= StringVar()

e1 = Entry(window, textvariable=dollars)
e1.grid(row=0, column=1)

t1 = Text(window, height = 5, width =15)
t1.grid(row=1, column=0)

t2 = Text(window, height = 5, width =15)
t2.grid(row=1, column=1)

t3 = Text(window, height = 5, width =15)
t3.grid(row=1, column=2)

window.mainloop()