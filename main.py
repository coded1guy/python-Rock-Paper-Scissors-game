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
def newGame():
    print(instructions)
    start()

options = ["R", "P", "S"]

def start():
    userChoice = input("pick an option between \"R\", \"P\" or \"S\": ")

newGame()
