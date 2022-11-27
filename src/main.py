import random

# function to input player choice and return its value
def getPlayerChoice():
    playerChoice = input("""Choose Your Move
    - 'r' for Rock
    - 'p' for Paper
    - 's' for Scissors
    Input: """)
    return playerChoice
# function to generate computer choice and return its value
def getComputerChoice():
    computerChoice = random.choice(['r', 'p', 's'])
    return computerChoice

# main
