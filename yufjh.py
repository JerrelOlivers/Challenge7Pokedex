import PySimpleGUI as sg
import mysql.connector



myDatabase = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "",
    database = "pokedex"
)
def insertData(values):
    pass

def editData(values):
    name = values["name"]
    attack = values["attack"]
    special = values["special"]
    defense = values["defense"]
    gender = values["gender"]
    pokemon_type = values["type"]

    sqlCommandEdit = "UPDATE pokemon set name = %s, attack = %s, special = %s, defense = %s, type = %s WHERE id = %s"

    cursor.execute(sqlCommandEdit, (attack, special, defense, gender, pokemon_type, idToEdit))
    myDatabase.commit()

cursor = myDatabase.cursor()

mainWindow = [
    [sg.Button("Insert Data")],
    [sg.Button("Edit Data")]
]

window = sg.Window("Pokedex", mainWindow)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Edit Data":
        idToEdit = sg.popup_get_text("Enter pokemon ID to edit", "Enter pokemon ID: ")

    cursor.execute("SELECT * FROM pokemon WHERE id = %s", (idToEdit,)) #na te hebben onderzocht bleek dat de komm een "tuple" hiervan maakt, en kreeg ik de error niet meer.
    pokemonData = cursor.fetchone()


#hier onder komt default_text=. Dit betekent (naar mijn idee althans) dat er tekst op het scherm komt, aangezien de tekst 
# zonder default_text niet in beeld komt.

#de [1] en dergelijken zorgen ervoor dat de data die op het scherm komt ook overeenkomt met die tabel ipv dat hij alle data laat zien
#per balk

    if pokemonData:
        editLayout = [
           [sg.Text("Name"), sg.InputText(key="name", default_text=pokemonData[1])],
                [sg.Text("Attack"), sg.InputText(key="attack", default_text=str(pokemonData[2]))],
                [sg.Text("Special"), sg.InputText(key="special", default_text=str(pokemonData[3]))],
                [sg.Text("Defense"), sg.InputText(key="defense", default_text=str(pokemonData[4]))],
                [sg.Text("Gender"), sg.InputText(key="gender", default_text=pokemonData[5])],
                [sg.Text("Type"), sg.InputText(key="type", default_text=pokemonData[6])]
        ]
        
        editWindow = sg.Window("Edit pokemon data", editLayout)
       
        editEvent, editValues = editWindow.read()

    
        if editEvent == "Save Changes":
                editData(editValues)
        editWindow.close()