from tkinter import *

# button = you click it, then it does stuff

def click():
    print("You clicked the button!")

window = Tk()

photo = PhotoImage(file='jill.png')

button = Button(window,
                text="click me!",
                command=click,
                image=photo)
button.pack()

window.mainloop()
