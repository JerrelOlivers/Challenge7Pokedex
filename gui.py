import PySimpleGUI as sg
from tkinter import *


# GUI layout

def layout():
    layout = [
        [sg.Text("Name"), sg.InputText(key="name")],
        [sg.Text("Attack"), sg.InputText(key="attack")],
        [sg.Text("Special"), sg.InputText(key="special")],
        [sg.Text("Defense"), sg.InputText(key="defense")],
        [sg.Text("Gender"), sg.InputText(key="gender")],
        [sg.Text("Type"), sg.InputText(key="type")],
        [sg.Button("Insert Data"), sg.Button("Close")]
]
    return layout

insertButton = Button(text="Insert Data")
if insertButton == True:
    layout()
    

# Create the GUI window
window = sg.Window("Pokemon Database", layout)

event, values = window.read()
