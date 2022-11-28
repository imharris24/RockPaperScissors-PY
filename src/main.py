import random

choice = ['r', 'p', 's']
# function to input player choice and return its value
def getPlayerChoice():
    playerChoice = input("""Choose Your Move
    - 'r' for Rock
    - 'p' for Paper
    - 's' for Scissors
    Input: """)[0]
    playerChoice = playerChoice.lower()
    while playerChoice not in choice:
        playerChoice = input("""Error: INVALID INPUT
        Input again: """)
        playerChoice = playerChoice.lower()
    return playerChoice
# function to generate computer choice and return its value
def getComputerChoice():
    computerChoice = random.choice(choice)
    return computerChoice
# function that returns result
def returnResult(player, computer):
    if player == computer:
        return [0, 0]
    elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return [1, 0]
    else:
        return [0, 1]
    
# main
