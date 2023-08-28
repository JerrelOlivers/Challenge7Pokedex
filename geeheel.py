import mysql.connector
import PySimpleGUI as sg

# Function to handle data insertion
def insertData(values):
    name = values["name"]
    attack = values["attack"]
    special = values["special"]
    defense = values["defense"]
    gender = values["gender"]
    pokemon_type = values["type"]
    
    # Insert data into the database (replace with your database code)
    cursor.execute(sql_command, (name, attack, special, defense, gender, pokemon_type))
    myDatabase.commit()

# Function to define the data entry layout
def dataEntryLayout():
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

# Connection string (replace with your database details)
myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pokedex"
)

# Create a cursor for the database
cursor = myDatabase.cursor()

# SQL command for data insertion (replace with your table structure)
sql_command = "INSERT INTO pokemon (name, attack, special, defense, gender, type) VALUES (%s, %s, %s, %s, %s, %s)"

# Main window layout
main_layout = [
    [sg.Button("Insert Data")],
    [sg.Button("Delete Data")],
    [sg.Button("Edit Data")]
]

# Create the main window
window = sg.Window("Pokedex", main_layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "Insert Data":
        data_window = sg.Window("Insert Pokemon Data", dataEntryLayout())

        data_event, data_values = data_window.read()

        if data_event == "Insert Data":
            insertData(data_values)
        
        data_window.close()

window.close()
