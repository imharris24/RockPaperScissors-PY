import random

# functions and variables for Rock, Paper, Scissors
choice = ['r', 'p', 's']
# function to return whole word instead of letter
def returnWord(letter):
    if letter == 'r':
        return 'Rock'
    elif letter == 'p':
        return 'Paper'
    elif letter == 's':
        return 'Scissors'
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
    return random.choice(choice)
# function that returns result
# [0, 0] = DRAW
# [1, 0] = Player WIN
# [0, 1] = Computer WIN
def returnResult(player, computer):
    print('Player: ', returnWord(player))
    print('Computer: ', returnWord(computer))
    if player == computer:
        return [0, 0]
    elif (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return [1, 0]
    else:
        return [0, 1]


# main
while True:
    result = returnResult(getPlayerChoice(), getComputerChoice())
    if result[0] == result[1]:
        print('It\'s a DRAW!')
    elif result[0] == 1:
        print('You WIN!')
    else:
        print('You LOSE!')
    input('\nPress Enter to Return...\n\n')
