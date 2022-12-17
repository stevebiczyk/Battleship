# PROJECT 3 - BATTLESHIPS

## Overview

My chosen project was to create a Battleships game that can be played inside the Python Terminal window.
The game was created using the Code Institute's Python Essentials Template and deployed on Heroku, displayed in a browser-based terminal window.

![Image of deployed project from Am I responsive](./assets/images/responsive.png)

The live game can be found here : <a href = "https://steveb-project3-battleships.herokuapp.com/">BattleShips</a>

#  
## Table of Contents

- [PROJECT 3 - BATTLESHIPS](#battleships)
- [Overview](#overview)
- [Table of Contents](#table-ofcontents)
- [Game Rules](#game-rules0)
- [Features](#features)
- [Design](#design)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

# Game Rules

The game starts by greeting the player and asking for their name. It displays the instructions for playing. Then the game begins by randomly generating 5 ships on both the player's and the computer's board. The position of the ships is denoted by the letter "S". The player is shown their board with the location of the ships on it.  They are also shown the computer's board but without being able to see the ships on it.

![Welcome Image](./assets/images/welcome_screen.png)

The game will then prompt the player to enter a row and column number of the location that they want to target. In the case where the location holds a battleship, the game will declare a successful hit and display the computer's board with the position marked with a " * ". If there is no battleship at the location, it is declared as a miss and is marked with a "x".

![Gameplay Image](./assets/images/gameplay_screen.png)

Following each turn by the player, the computer has an automated go.  The result is displayed on the player's board in an identical way to the player's results. The score is displayed showing how many battleships have been hit.

There are 10 rounds where both the player and the computer will try to find all of the opponent's ships. In the case where the 10 rounds pass without all 5 ships being hit, the game will state who has had the most hits and name them as the winner. If the score is the same then it will declare a draw.  It then gives the option to play again or exit.

![Player Win](./assets/images/final_pwin.png) ![Computer Win](./assets/images/final_cwin.png) 
![Draw Result](./assets/images/final_draw.png)

It is also possible to win by hitting all 5 ships before the end of the game, however it is very unlikely to happen. However I checked what would happen by extending the turn counter to 20 turns.

![5 Hits Win](./assets/images/win_5hits.png)



# Features

## Existing Features

* Personalised introductory message that states the games rules
* Generation of boards and random generation of ships on the boards
* Turn by turn play against the computer
* Target selection by the player
* Turns and scores are tracked to decide the winner
* Input is validated for referencing outside of the board dimensions, entering the wrong data type and repeated targeting of the same location.

## Planned Features

* Allowing the player to select their ships positions.
* Adding decorative features such as ASCII art and colourful text.
* Allowing the player to change the difficulty level by changing the size of the board, the size and number of ships, etc.
* Creating additional levels of the game with score tracking and leader board
* The game could include a feature for saving and loading games, allowing players to pick up where they left off at a later time.

# Design

The requirement was to create and deploy a terminal based battleship game using the Python programming language.

## Design Criteria

* The game should be easy to understand and play for users, with clear instructions provided at the start of the game.
* The game should be visually appealing and easy to navigate, using ASCII art or other similar techniques to display the game board and other relevant information.
* The game should be well-tested and free of bugs or other issues that could negatively impact the player's experience.
* The game should be written in a way that is easy to understand and maintain, with clear and well-documented code.

# Testing

## Manual Testing

Defensive design principles were followed. The code has several built-in functions to stop the user from entering the wrong type or range of input.
* When selecting a target row and column the user is prompted to input a number between 1 and 5 for each. This input is checked for data range and data type.

 ![Input Validation](./assets/images/input_validation.png)

* At the end of the game the user is requested to input either "y" to play again or "n" to exit the game. This input is also validated and any other input besides these two letters is rejected. The user is then requested to provide the correct input.

* A spell checker was also used to find and correct any spelling mistakes in the Readme file.

![End of Game Validation](./assets/images/endgame_validation.png) 


## PEP8 Validator Testing

PEP8 validator was used within the Gitpod Workspace. These were the required steps:
* Run the command pip3 install pycodestyle.
* In the workspace, press Ctrl+Shift+P.
* Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.
* Select pycodestyle from the list.
* PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside the terminal.

The most common issues encountered were the line length exceeding the limit, not enough blank lines between functions and trailing whitespaces, these were all corrected.

![PEP8 Validation](./assets/images/pep8_validation.png)


# Technologies Used

* [GitHub](https://github.com/) This was used for version control and to host the website, so it is viewable to the public.
* [GitPod](gitpod.io) This was used as an IDE, or the Integrated Development Area.
* [Pycodestyle](https://pypi.org/project/pycodestyle/) was used to check for code formatting errors.
* [Python](https://www.python.org/) The game itself is written in python and held in the run.py file.
* [Heroku](https://www.heroku.com) Heroku was used to deploy the website as python is a backend language and the terminal was needed to display the game.
* [Am I Responsive](https://ui.dev/amiresponsive) Used to test responsiveness of the game at different screen sizes.

# Deployment

* The project was deployed on the Heroku website using Code Institute's terminal template. Here are the steps I have taken to successfully deploy the project: 
    
    1. Create a new repository from the Code Institute Python template.
    2. Create a new Heroku account / Register.
    3. Create a new Heroku App.
    4. Set the Config Vars to PORT 8000 in the Settings tab.
    4. Set build packs to Python and NodeJS in this order.
    5. Link the Heroku App into the repository on GitHub.
    6. Deploy the App.


# Acknowledgements and Credits

* My mentor Dick Vlaanderen for his input and ideas.
* The Code Institute Tutor Support for their help with my many project related questions.
* For the following YouTube channels: [Knowledge Mavens](https://www.youtube.com/@KnowledgeMavens), [CodingTutorials360](https://www.youtube.com/@CodingTutorials360) and [Dr Codie](https://www.youtube.com/@DrCodie).
* For the following websites: [Copy Assingnment](https://copyassignment.com/battleship-game-code-in-python/) and [Trinket.io](https://trinket.io/python/051179b6d3) for general ideas on the structure and functions of the game, such as board generation and indexing, etc. 
* Google Search was used to find answers to many general Python related questions. Most of the answers came from [Stack Overflow](https://stackoverflow.com/) and [W3 Schools](https://www.w3schools.com/python/python_reference.asp)
