import random

instructions = """
------------------------------------
Here is the instruction for the game
------------------------------------

You'll be asked to pick an option between \"R\", \"P\" or \"S\"
Where: \n
\"R\" for \"rock\",
\"P\" for \"paper\",
\"S\" for \"scissors\"

the computer then chooses a random option,
then the winner is chosen.

-------------------
Have fun with it :)
-------------------
"""

def new_game():
    print(instructions)
    start()

options = ["R", "P", "S"]
user_choice = None
computer_choice = None
# shows computer choice
def show_computer_choice():
    computer_choice = random.choice(options)
    # show the user what the computer chose
    if computer_choice == "R":
        print("Computer chose Rock!")
    elif computer_choice == "P":
        print("Computer chose Paper!")
    else:
        print("Computer chose Scissors!")

def start():
    user_choice = input("pick an option between \"R\", \"P\" or \"S\": ").upper()
    # show the user what they chose
    if user_choice == "R":
        print("You chose Rock!")
        show_computer_choice()
        validate()
    elif user_choice == "P":
        print("You chose Paper!")
        show_computer_choice()
        validate()
    elif user_choice == "S":
        print("You chose Scissors!")
        show_computer_choice()
        validate()
    else:
        print("invalid choice, you are to chose an option between \"R\", \"P\" or \"S\".")

def validate():
    # if the user's choice is the same as the computer's choice
    if user_choice == "R" and computer_choice == "R" or user_choice == "P" and computer_choice == "P" or user_choice == "S" and computer_choice == "S":
        print("Draw!!!")
        to_start_again = input("do you want to start again (y/n): ")
        if to_start_again == "y" or to_start_again == "yes":
            start()
        else:
            print("The game ended in a draw")
    # if the user chooses Rock and the computer chooses Paper
    elif user_choice == "R" and computer_choice == "P":
        loss()    
    # if the user chooses Rock and computer chooses Scissors
    elif user_choice == "R" and computer_choice == "S":
        win()
    # if the user chooses Scissors and computer chooses Paper
    elif user_choice == "S" and computer_choice == "P":
        win()
    # if the user chooses Scissors and computer chooses Rock
    elif user_choice == "S" and computer_choice == "R":
        loss()
    # if the user chooses Paper and computer chooses Rock
    elif user_choice == "P" and computer_choice == "R":
        win()
    # if the user chooses Paper and computer chooses Scissors
    elif user_choice == "P" and computer_choice == "S":
        loss()
# this runs when the user wins a game        
def win():
    print("You Win!!!")
    print("Congratulations, You won this round")
    to_play_again = input("do you want to play again (y/n): ")
    if to_play_again.lower() == "y" or to_play_again.lower() == "yes":
        start()
    elif to_play_again.lower() == "n" or to_play_again.lower() == "no":
        print("The game ended in a win")

def loss():
    print("Computer Wins!!!")
    print("sorry, you lost this round")
    to_play_again = input("do you want to play again (y/n): ")
    if to_play_again.lower() == "y" or to_play_again.lower() == "yes":
        start()
    elif to_play_again.lower() == "n" or to_play_again.lower() == "no":
        print("The game ended in a loss")

new_game()
