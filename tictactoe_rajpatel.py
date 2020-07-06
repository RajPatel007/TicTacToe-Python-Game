# Tic-Tac-Toe Game
# Summary: This game begins with empty 3X3 matrix board. Player(user) is an 'X' and Computer(user) is an 'O'.
# The playGame function plays the game us vs. computer(random input) and isWinner function finds the winning strategy.
# The computerMove function has the winning strategy for the computer(random).
#
# Created by Raj Patel

# Imported libraries/modules
import random
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]                           # empty board

def clearBoard():                                                               # clearBoard function clears the board
    for i in range(len(board)):
        board[i] = " "
    playGame()                                                                  # playGame function call plays the game again

def printBoard():                                                               # printBoard function prints 3X3 matrix board
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
        
def isWinner(board,player):                                                     # isWinner function checks the winning configurations for players
    if (board[0] == player and board[4] == player and board[8] == player) or \
       (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player):
        return True
    else:
        return False
    
def isBoardFull(board,player):                                                  # isBoardFull function checks whether the board is full
    if " " in board:
        return False
    else:
        return True

def computerMove(board,player):                                                 # computerMove function checks the winning strategy for computer player 'O'
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if isWinner(board, player):
                return i
            else:
                board[i] = " "
    
    while True:
        move = random.randint(0,8)                                              # move takes random moves for the computer user
        if board[move] == " ":
            return move
            break
        
def playGame():                                                                 # playGame function is the actual game against 'X' vs. 'O'
    while True:
        printBoard()                                                            
        try:                                                                    # try block checks if the user enters valid value for the move
            index = int(input('Please enter index-value to display X:'))
        except ValueError:
            print('Invalid Literal for int, please enter value between 0 and 8')
        else:
            if index >= 0 and index <= 8:
                if board[index] == " ":
                    board[index] = "X"
                else:
                    print("Sorry, that space is not empty!")
                    time.sleep(1)
            else:
                print('Wrong index value, please select from 0 through 8')
        
        if isWinner(board, "X"):                                                # isWinner function call, which checks if the user('X') is winning!
            printBoard()
            print("The player wins the game!")
            while True:
                response = input("Do you want to play again? (yes or no): ")    # if the user (X) wins, it has chance to play the game again
                if response == "yes":
                    return clearBoard()                                         # clearBoard function call makes empty board
                else:
                    return False
                
        if isBoardFull(board, "X"):                                             # isBoardFull function call, which checks if the board is full, then game tie
            printBoard()
            print("The game is Tie!")
            break
            
        choice = computerMove(board, "O")                                       # choice takes a random move/index for the computer
        
        if board[choice] == " " or board[choice] != "X":                        
            board[choice] = "O"
        elif board[choice] == "X":
            choice += 1
            board[choice] = "O"
            time.sleep(1)
                
        if isWinner(board, "O"):                                                # isWinner function call, which checks if the computer('O') is winning!
            printBoard()
            print("The computer wins the game!")
            print("Game Over!")
            break
        
        if isBoardFull(board, "O"):                                             # isBoardFull function call, which checks if the board is full and last input 'O',
            print_board()                                                       # then game tie
            print("The game is Tie!")
            break
        
if __name__ == '__main__': clearBoard()
