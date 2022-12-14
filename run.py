from random import randint  # importing randint function

PLAYER_BOARD = []
COMPUTER_BOARD = []
HIDDEN_BOARD = []
TURN_COUNTER = 0
player_name = ""
player_score = 0
computer_score = 0


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
    return player_name
    
# Use the player_name variable later in the program
player_name = welcome_msg()
print(f"Let's get started, {player_name}!")


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
    """
    Display both game boards at the start of each round
    """

    # create_board(PLAYER_BOARD)
    # place_ships(PLAYER_BOARD)
    print(f"This is the {player_name}'s board")
    print_board(PLAYER_BOARD)
    # create_board(HIDDEN_BOARD)
    # place_ships(HIDDEN_BOARD)
    # create_board(COMPUTER_BOARD)
    print("This is the computer's board")
    print_board(COMPUTER_BOARD)


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

    global computer_score

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
    return computer_score
        

def player_target(board):
    """
    Player target selection
    """
    turns = 0
    global player_score

    # Get input from player
    while True:
        try:
            target_row = int(input("Select a row:(Number between 1 and 5)\n"))
            target_column = int(
                input("Select a column:(Number between 1 and 5) \n"))

            # Check if target is valid
            if target_row < 1 or target_row > 5 or target_column < 1 or target_column > 5:
                print("Invalid target. Please choose a row and column between 1 and 5.")
                continue

            # Check if target has been selected before
            if HIDDEN_BOARD[target_row-1][target_column-1] == "*" or HIDDEN_BOARD[target_row-1][target_column] == "x":
                print("You already targeted this spot, aim again")
                turns = turns + 1
                continue

            # Update boards and score based on target
            if HIDDEN_BOARD[target_row-1][target_column-1] == "S":
                HIDDEN_BOARD[target_row-1][target_column-1] = "*"
                COMPUTER_BOARD[target_row-1][target_column-1] = "*"
                print("Congratulations! You hit the computer's ship!")
                print_boards(board)  # to check hit
                turns = turns + 1
                player_score += 1
            else:
                HIDDEN_BOARD[target_row-1][target_column-1] == "."
                COMPUTER_BOARD[target_row-1][target_column-1] = "x"
                print("You missed! Better luck next time!")
                print_boards(board)
                # print_board(HIDDEN_BOARD)
            return player_score

        except ValueError:
            print("Error with input value")
            print("Please type in a number")


def hit_counter(board):

    # Keeping track of ships that have been hit

    hits = 0
    for row in board:
        for column in row:
            if column == "*":
                count += 1
    return count


def play_again():
    while True:
        response = input("Would you like to play again? (y/n) ")
        if response == "y":
            # Start the game again here
            return True
        elif response == "n":
            print("Thanks for playing! Goodbye.")
            return False
        else:
            print("Invalid response. Please enter 'y' to play again or 'n' to quit.")


def quit():
    # Add code to clean up and exit the game here
    print("Thanks for playing! Goodbye.")
    exit()


def play_game():
    # Add code to start and play the game here

    while True:
        play_game()
    if not play_again():
        quit()


# def ships_hit():

def game_loop():

    welcome_msg()
    create_board(PLAYER_BOARD)
    place_ships(PLAYER_BOARD)
    print_board(PLAYER_BOARD)
    print(f"This is the {player_name}'s board")
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
    hit_counter(board)


game_loop()


# Remaining functions/features to be added or completed

# Turn counter for 10 turns
# Start new round or exit game prompt after each turn
# Game boards with changes displayed at the end of each round or start of new round
# Check how many ships are hit
# Score counter for both player and computer
# Deciding winner either by sinking all ships or higher score
# Final message stating winner
