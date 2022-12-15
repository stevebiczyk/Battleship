from random import randint  # Importing randint function

PLAYER_BOARD = []
COMPUTER_BOARD = []
HIDDEN_BOARD = []
PLAYER_NAME = ""
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
TURN_COUNTER = 0


def welcome_msg():
    """
    Name input for player and welcome message
    """
    print("Welcome player!")
    PLAYER_NAME = input("Please type in your name and press Enter: \n")
    print(f"Hi {PLAYER_NAME}, welcome to Battleships!")
    print("Your goal is to beat the Computer.")
    print("You have 5 ships each, sink the opponent's ships first to win!")
    print("Make your selection by choosing a number between 1 and 6")
    print("The board is 5 rows and 5 columns.")
    print("Hits are marked with * and misses are x")
    return PLAYER_NAME


# Use the PLAYER_NAME variable later in the program
PLAYER_NAME = welcome_msg()
print(f"Let's get started, {PLAYER_NAME}!")


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
    print(f"This is the {PLAYER_NAME}'s board")
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
            ship_row, ship_column = randint(0, len(board) - 1), randint(
                0, len(board) - 1
            )
        board[ship_row][ship_column] = "S"


def computer_target(board):
    """
    Choose a target on the player's board and update the game state.

    This function randomly selects a row and column on the player's board to
    target. It then checks if the target has been selected before, or contains
    a ship. Based on the result, it updates the game state (boards and score),
    and prints a message to the player.
    """
    global COMPUTER_SCORE

    comp_row, comp_column = randint(
        0, len(board) - 1), randint(0, len(board) - 1)
    if (
        PLAYER_BOARD[comp_row][comp_column] == "*"
        or PLAYER_BOARD[comp_row][comp_column] == "X"
    ):
        comp_row = randint(0, len(board) - 1)
        comp_column = randint(0, len(board) - 1)
    elif PLAYER_BOARD[comp_row][comp_column] == "S":
        print("Player, your battleship has been hit!")
        print(f"The computer hit row {comp_row + 1} \
        and column {comp_column + 1}")
        PLAYER_BOARD[comp_row][comp_column] = "*"
        COMPUTER_SCORE += 1
    else:
        print(f"The computer hit row {comp_row + 1} \
        and column {comp_column + 1}")
        print("You're lucky player, the computer missed!")
        PLAYER_BOARD[comp_row][comp_column] = "X"
    return COMPUTER_SCORE


def player_target(board):
    """
    Select a target on the computer's board and update the game state.
    This function prompts the player to choose a row and column on the
    computer's board to target. It then checks if the target is valid,
    has been selected before, or contains a ship. Based on the result,
    it updates the boards and score, and prints a message to the player.
    """
    turns = 0
    global PLAYER_SCORE

    # Get input from player
    while True:
        try:
            target_row = int(input("Select a row:(Number between 1 and 5)\n"))
            target_column = int(
                input("Select a column:(Number between 1 and 5) \n"))
            # Check if target is valid
            if (
                target_row < 1
                or target_row > 5
                or target_column < 1
                or target_column > 5
            ):
                print("Invalid target. \
                     Please choose a row and column between 1 and 5.")
                continue

            # Check if target has been selected before
            if (
                HIDDEN_BOARD[target_row - 1][target_column - 1] == "*"
                or HIDDEN_BOARD[target_row - 1][target_column - 1] == "x"
            ):
                print("You already targeted this spot, aim again")
                turns = turns + 1
                continue

            # Update boards and score based on target
            if HIDDEN_BOARD[target_row - 1][target_column - 1] == "S":
                HIDDEN_BOARD[target_row - 1][target_column - 1] = "*"
                COMPUTER_BOARD[target_row - 1][target_column - 1] = "*"
                print("Congratulations! You hit the computer's ship!")
                print_boards(board)  # to check hit
                turns = turns + 1
                PLAYER_SCORE += 1
            else:
                HIDDEN_BOARD[target_row - 1][target_column - 1] == "X"
                COMPUTER_BOARD[target_row - 1][target_column - 1] = "X"
                print("You missed! Try again.")
                print_boards(board)
                #  print_board(HIDDEN_BOARD)
            return PLAYER_SCORE

        except ValueError:
            print("Error with input value")
            print("Please type in a number")


def hit_counter(board):
    """
    Count the number of ships that have been hit on the given board.
    This function loops through the rows and columns of the given board and
    counts the number of times the "*" character appears, which indicates that
    a ship has been hit.
    """
    hits = 0
    for row in board:
        for column in row:
            if column == "*":
                hits += 1
    return hits


def play_again():
    """
    Prompt the player to play again or quit the game.
    This function asks the player if they want to play again, and returns
    `True` if they choose to play again, or `False` if they choose
     to quit the game.
    """
    while True:
        response = input("Would you like to play again? (y/n) ")
        if response == "y":
            # Start the game again here
            return True
        elif response == "n":
            print("Thanks for playing! Goodbye.")
            return False
        else:
            print("Invalid response. Please enter 'y' \
                 to play again or 'n' to quit.")


def quit():
    """
    Exit the game with a goodbye message.
    """
    print("Thanks for playing! Goodbye.")
    exit()


def play_game():
    """
    Start and play the game.
    This function starts the game by calling the `game_loop` function, which
    runs the main gameplay loop. After each game, it prompts the player to
    play again or quit the game. If the player chooses to play again, the
    `game_loop` function is called again, otherwise the game ends.
    """

    while True:
        play_game()
    if not play_again():
        quit()


# def ships_hit():


def game_loop():
    """
    Run the main gameplay loop for the battleship game.
    This function initializes the game state, creates and prints the boards,
    and prompts the player and computer to take turns selecting targets. It
    continues the gameplay loop until one player's ships are all hit or the
    maximum number of turns has been reached. After the game ends, it calls the
    `end_game` function to display the final score and offer the player the
    option to play again.
    """

    global TURN_COUNTER
    global PLAYER_BOARD
    global COMPUTER_BOARD
    global HIDDEN_BOARD
    global PLAYER_SCORE
    global COMPUTER_SCORE

    # Create and print the boards

    PLAYER_BOARD = []
    COMPUTER_BOARD = []
    HIDDEN_BOARD = []
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0
    TURN_COUNTER = 0
    create_board(PLAYER_BOARD)
    place_ships(PLAYER_BOARD)
    print_board(PLAYER_BOARD)
    print(f"This is the {PLAYER_NAME}'s board")
    create_board(HIDDEN_BOARD)
    place_ships(HIDDEN_BOARD)
    print("This is the hidden board")
    create_board(COMPUTER_BOARD)
    print_board(COMPUTER_BOARD)
    print("This is the computer's board")
    print("The ships have been placed, let the game begin!")

    # Run the gameplay loop until the game ends

    while (
        hit_counter(HIDDEN_BOARD) < 5
        and hit_counter(PLAYER_BOARD) < 5
        and (TURN_COUNTER <= 9)
    ):
        print("---------------new Round-----------------")
        print("your score " + str(PLAYER_SCORE))
        print("Computer score " + str(COMPUTER_SCORE))
        TURN_COUNTER = TURN_COUNTER + 1
        player_target(HIDDEN_BOARD)
        computer_target(PLAYER_BOARD)
        hit_counter(HIDDEN_BOARD)
    end_game()


def end_game():
    """
    End the game and display the final score.
    This function prints the number of ships hit by the player and the
    computer. It then determines the winner (or if it's a draw)
    and offers the player the option to play again by calling
    the `play_again` function. If the player
    chooses to play again, the `game_loop` function
    is called to start a new game.
    """
    print("Number of ships you hit " + str(PLAYER_SCORE))
    print("Number of ships hit by computer " + str(COMPUTER_SCORE))
    if PLAYER_SCORE < COMPUTER_SCORE:
        print("The computer wins! Better luck next time.")
    elif PLAYER_SCORE > COMPUTER_SCORE:
        print("Congratulations! You are the winner!!!")
    elif PLAYER_SCORE == COMPUTER_SCORE:
        print("The game is over, it's a draw.")
    if play_again():
        game_loop()


game_loop()
