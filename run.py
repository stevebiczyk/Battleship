from random import randint

PLAYER_BOARD = []
COMPUTER_BOARD = []
HIDDEN_BOARD = []
# player_score = 0
# computer_score = 0


def welcome_msg():
    """
    Name input for player and welcome message
    """
    print("Welcome player!")
    player_name = input("Please type in your name and press Enter: \n")
    print(f"Hi {player_name}, welcome to Battleships!")
    print("Your goal is to beat the Computer.")
    print("You have 5 ships each, sink the opponent's ships first to win!")
    print("Make your selection by choosing a number between 1 and 6")
    print("The board is 5 rows and 5 columns.")
    print("Hits are marked with * and misses are x")


def create_board(board):
    """
    Create the game board from the empty list.
    This function generates a nested list.
    It consist of 5 rows and 5 columns of the letter "O"
    """
    for x in range(5):
        board.append(["."] * 5)
    return board


def print_board(board):
    """
    Display the game board
    """
    print("  1 2 3 4 5 ")
    print("  ---------")
    row_number = 1
    for row in board:
        print(row_number, (" ").join(row))
        row_number += 1


def print_boards(board):
    # create_board(PLAYER_BOARD)
    # place_ships(PLAYER_BOARD)
    print_board(PLAYER_BOARD)
    print("This is the player's board")
    # create_board(HIDDEN_BOARD)
    # place_ships(HIDDEN_BOARD)
    # create_board(COMPUTER_BOARD)
    print_board(COMPUTER_BOARD)
    print("This is the computer's board")


def gen_random_num(board):
    """
    Generate random number within the dimensions of the board.
    Minus 1 as list index stars at 0 instead of 1
    Used to place the ships in random locations
    """
    return randint(0, len(board) - 1)


def place_ships(board):
    """
    Randomly generate and place 5 ships on the board.
    A counter keeps track of the number of ships.
    Duplicate ship placement is also handled by the counter.
    """
    for ship in range(5):
        ship_row, ship_column = randint(
            0, len(board) - 1), randint(0, len(board) - 1)
        while board[ship_row][ship_column] == "S":
            ship_row, ship_column = randint(
                0, len(board) - 1), randint(0, len(board) - 1)
        board[ship_row][ship_column] = "S"


def computer_target(board):

    computer_score = 0

    comp_row, comp_column = randint(
        0, len(board) - 1), randint(0, len(board) - 1)
    if (PLAYER_BOARD[comp_row][comp_column] == "*" or
            PLAYER_BOARD[comp_row][comp_column] == "X"):
        comp_row = randint(0, len(board) - 1)
        comp_column = randint(0, len(board) - 1)
    elif PLAYER_BOARD[comp_row][comp_column] == "S":
        print("Player, your battleship has been hit!")
        print(
            f"The computer hit row {comp_row + 1}"
            f" and column {comp_column + 1}")
        PLAYER_BOARD[comp_row][comp_column] = "*"
        computer_score += 1
    else:
        print(
            f"The computer hit row {comp_row + 1}"
            f" and column {comp_column + 1}")
        print("You're lucky player, the computer missed!")
        PLAYER_BOARD[comp_row][comp_column] = "X"
        print_boards(board)  # to check state of game
        print(computer_score)  # to check the score


def player_target(board):
    """
    Player target selection
    """
    turns = 0
    player_score = 0
    for turn in range(10):
        try:
            target_row = int(input("Select a row: (Number between 1 and 5)\n"))
            target_column = int(input("Select a Column: (Number between 1 and 5) \n"))

            if target_row == HIDDEN_BOARD [ship_row] and target_column == HIDDEN_BOARD [ship_column]:
                COMPUTER_BOARD[target_row][target_column] = "*"
                print("Congratulations! You hit the computer's ship!")
                print_boards(board)
                turns = turns + 1
                player_score += 1
                break
            elif (target_row < 1 or target_row > 5) or \
                    (target_column < 1 or target_column > 5):
                print("Your selection is out of range! Try again")
                turns = turns + 1
            else:
                board[target_row][target_column] = "x"
                print("You Missed! Try Again")
                print_boards(board)
                turns = turns + 1

        except ValueError:
            print("Error with input value")
            print("Please type in a number")
            continue


# validate_player_target():
# def computer_target_():
# def ships_sunk():
welcome_msg()
create_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)
print_board(PLAYER_BOARD)
print("This is the player's board")
create_board(HIDDEN_BOARD)
place_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)
print("This is the hidden board")
create_board(COMPUTER_BOARD)
print_board(COMPUTER_BOARD)
print("This is the computer's board")
print("The ships have been placed, let the game begin!")
player_target(HIDDEN_BOARD)
computer_target(PLAYER_BOARD)


# Remaining functions/features to be added

# Player selection for placing the shot
# Random selection for computer's shot
# Check how many ships are hit
# Score counter
# Round counter
