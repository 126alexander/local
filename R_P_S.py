# Python Random & Playsound Modules
import random
from playsound import playsound

# Function
def again():
  # Variables
    dices = 0
    roll_again = print()
    while dices == 0:
    	# User's choice of how many dices they want to roll
        chosen_dices = int(input("How many dices do you want to roll? (from 1 to 5): "))
        # If the user choose a number between 1 and 5, break out of the loop
        if chosen_dices > 0 and chosen_dices < 6:
            break
  
    # If the user choose (any number) dice(s), generate a random number from 1 to 6 and continue until we meet the user's needs
    if chosen_dices == 1:
        playsound('Dice shake.mp3')
        playsound("Dice roll.mp3")  
        while dices < 1 :
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 2:
        playsound('Dice shake.mp3')
        playsound("Dice roll.mp3")  
        while dices < 2 :
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 3:
        playsound('Dice shake.mp3')
        playsound("Dice roll.mp3")  
        while dices < 3 :
            rolls = random.randint(1, 6)          
            print(rolls)
            dices +=1

    elif chosen_dices == 4:
        playsound('Dice shake.mp3')
        playsound("Dice roll.mp3") 
        while dices < 4 :
            rolls = random.randint(1, 6)
            print(rolls)
            dices +=1

    elif chosen_dices == 5:
        playsound('Dice shake.mp3')
        playsound("Dice roll.mp3")  
        while dices < 5 :
            rolls = random.randint(1, 6)     
            print(rolls)
            dices +=1
  
    # Asking the user if he wants to roll again
    print("Do you want to roll again?")
    while roll_again != "Yes" or roll_again != "No":
        roll_again = input("Yes | No: ").lower().capitalize()
        # If yes, then go back to the function
        if roll_again == "Yes":
            again()
            break
        # If no, then say goodbye and exit
        if roll_again == "No":
            print("Goodbye")
            break
# End of function
again()