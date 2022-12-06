# random function for generationg the ships on the board
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
    """
    Create the game board from the empty list.
    This function generates a nested list.
    It consist of 5 rows and 5 columns of the letter "O"
    """
    for x in range(5):
        board.append(["O"] * 5)
    return board


def print_board(board):
    """
    Display the game board
    """
    for row in board:
        print((" ").join(row))


def gen_random_num(board):
    """
    Generate random number within the dimensions of the board.
    Used to place the ships in random locations
    """
    return randint(0, len(board) - 1)


welcome_msg()
create_board(player_board)
print_board(player_board)
print("This is player's board")
create_board(computer_board)
print_board(computer_board)
print("This is computer's board")



# Place ships on the board
# Player selection for placing the shot
# Random selection for computer's shot
# Check how many ships are hit
# Round counter