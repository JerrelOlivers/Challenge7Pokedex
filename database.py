import mysql.connector
import tkinter as tk
from tkinter import simpledialog

# Function to handle data insertion
def insertData():
    # Input from the user using popup windows
    name = simpledialog.askstring("Input", "Enter the name of the encountered pokemon: ")
    attack = simpledialog.askstring("Input", "Enter the attacking stats of the encountered pokemon: ")
    special = simpledialog.askstring("Input", "Enter the special stats of the encountered pokemon: ")
    defense = simpledialog.askstring("Input", "Enter the defending stats of the encountered pokemon: ")
    gender = simpledialog.askstring("Input", "Enter the gender of the encountered pokemon: ")
    pokemon_type = simpledialog.askstring("Input", "Enter the element of the encountered pokemon: ")

    # SQL command to insert data
    sql_command = "INSERT INTO pokemon (name, attack, special, defense, gender, type) VALUES (%s, %s, %s, %s, %s, %s)"

    # Establish a connection to the database
    myDatabase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pokedex"
    )

    # Create a cursor
    mycursor = myDatabase.cursor()

    # Execute the command with the user input
    mycursor.execute(sql_command, (name, attack, special, defense, gender, pokemon_type))

    # Commit the changes
    myDatabase.commit()
    
#maakt de window
window = tk.Tk()

# Create a button
button = tk.Button(window, text="Insert Data", command=insertData)
button.pack()

# Show the window
window.mainloop()
