import mysql.connector
from tkinter import *
import PySimpleGUI as sg


def insertData():
    name = values["name"]
    attack = values["attack"]
    special = values["special"]
    defense = values["defense"]
    gender = values["gender"]
    pokemon_type = values["type"]    

    cursor.execute(sqlCommandInsert, (name, attack, special, defense, gender, pokemon_type))
    myDatabase.commit()

def deleteData():
    return None

def editData(values):
    name = values["name"]
    attack = values["attack"]
    special = values["special"]
    defense = values["defense"]
    gender = values["gender"]
    pokemon_type = values["type"]

    # Use SQL to update the record based on the Pokemon's name
    sqlCommandEdit = "UPDATE pokemon SET name = %s, attack = %s, special = %s, defense = %s, gender = %s, type = %s WHERE id = %s"

    # Execute the SQL command with the name as the unique identifier
    cursor.execute(sqlCommandEdit, (attack, special, defense, gender, pokemon_type))
    myDatabase.commit()


def dataInsertLayout():
    insertDataLayout = [
        [sg.Text("Name"), sg.InputText(key="name")],
        [sg.Text("Attack"), sg.InputText(key="attack")],
        [sg.Text("Special"), sg.InputText(key="special")],
        [sg.Text("Defense"), sg.InputText(key="defense")],
        [sg.Text("Gender"), sg.InputText(key="gender")],
        [sg.Text("Type"), sg.InputText(key="type")],
        [sg.Button("Insert Data"), sg.Button("Close")]
    ]
    return insertDataLayout

def dataEditLayout():
    dataEditLayout = [
        [sg.Text("Name"), sg.InputText(key="name")],
        [sg.Text("Attack"), sg.InputText(key="attack")],
        [sg.Text("Special"), sg.InputText(key="special")],
        [sg.Text("Defense"), sg.InputText(key="defense")],
        [sg.Text("Gender"), sg.InputText(key="gender")],
        [sg.Text("Type"), sg.InputText(key="type")],
        [sg.Button("Save Changes"), sg.Button("Cancel")]
    ]
    return dataEditLayout

#connection string
myDatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pokedex"
)


#cursor voor de database
cursor = myDatabase.cursor()



#command
sqlCommandInsert = "INSERT INTO pokemon (name, attack, special, defense, gender, type) VALUES (%s, %s, %s, %s, %s, %s)"
sqlCommandDelete = ""
sqlCommandEdit = "UPDATE pokemon SET attack=%s, special=%s, defense=%s, gender=%s, type=%s WHERE name=%s"

#main window
main_window = [
    [sg.Button("Insert Data")],
    [sg.Button("Delete Data")],
    [sg.Button("Edit Data")]
]


window = sg.Window("Pokedex", main_window)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "Insert Data":
        data_window = sg.Window("Insert Pokemon Data", dataInsertLayout())

        data_event, data_values = data_window.read()

        if data_event == "Insert Data":
            insertData(data_values)
        
        data_window.close()
    if event == "Edit Data":
        data_window = sg.Window("Edit Pokemon Data", dataEditLayout())

        data_event, data_values = data_window.read()

        if data_event == "Save Changes":
            editData(data_values)
            data_window.close()

window.close()

