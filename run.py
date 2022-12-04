# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

player_board = []
computer_board = []
hidden_board = []


def welcome_msg():
    """
    Name input for player and welcome message
    """
    player_name = input("Please type in your name and press Enter: \n")
    print(f"Hi {player_name}, welcome to Battleships!")
    print("Your goal is to beat the Computer.")
    print("You have 5 ships each, whoever sinks the opponent's ship is the winner!")
    print("Make your selection by choosing a number between 1 and 6")
    print("The board is 6 columns and 6 rows. Hits are marked with @ and misses are X")


def create_board(board):
    for x in range(6):
        board.append(["O"] * 6)
    return board


def print_board(board):
    """
    Display the game board
    """
    for row in board:
        print((" ").join(row))


welcome_msg()
create_board(player_board)
print_board(player_board)
print("This is player's board")
create_board(computer_board)
print_board(computer_board)
print("This is computer's board")

