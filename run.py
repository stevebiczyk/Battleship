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
    Minus 1 as list index stars at 0 instead of 1
    Used to place the ships in random locations
    """
    return randint(0, len(board) - 1)


def place_ships(board):
    """
    Randomly generate and place 5 ships on the board.
    A counter keeps track of the number of ships.
    """
    num_of_ships = 0
    while num_of_ships < 4:
        num_of_ships = 0
        ship_col = gen_random_num(board)
        ship_row = gen_random_num(board)
        board[ship_row][ship_col] = " S "
        for row in board:
            num_of_ships += row.count(" S ")
        print(num_of_ships)


welcome_msg()
create_board(player_board)
print_board(player_board)
print("This is player's board")
create_board(computer_board)
print_board(computer_board)
print("This is computer's board")
place_ships(player_board)
place_ships(computer_board)
print("The ships have been placed, let's begin!")


# Place ships on the board
# Player selection for placing the shot
# Random selection for computer's shot
# Check how many ships are hit
# Round counter
