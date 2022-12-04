# Your code goes here.
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

board = []

def create_board(board):
    for x in range(7):
        board.append(["O"] * 7)


def print_board(board):
    for row in board:
        print((" ").join(row))


print("Let's play Battleship!")
create_board(board)
print_board(board)