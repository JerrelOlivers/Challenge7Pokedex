import random

turns = 0

chosenNumber = random.randint(1, 100)

def yourChoice():
    return int(input("Choose a number between 1 and 100: "))

while True:  # Keep looping until the guess is correct
    yourGuess = yourChoice()  # Ask the user for their guess
    turns += 1
    
    if yourGuess > chosenNumber:
        print("Lower!")
    elif yourGuess < chosenNumber:
        print("Higher!")
    else:
        print("Wow, that was amazing! You did it in", turns, "turns!")
        break  # Exit the loop because the guess is correct
