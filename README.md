# PROJECT 3 - BATTLESHIP

## Overview

My chosen project was to create a Battleships game that can be played inside the Python Terminal window.
The game was created using the Code Institute's Python Essentials Template and deployed on Heroku, displayed in browser-based terminal window.

![ScreenShot](./readme-images/responsive.png)

The live game can be found here : <a href = "https://steveb-project3-battleships.herokuapp.com/">BattleShips</a>

#  
## Table of Contents

- [BATTLESHIPS](#battleships)
  - [Overview](#overview)
  - [Table of contents](#table-ofcontents)
  - [Game Rules](#game-rules0)
  - [Features](#features)
  - [Design](#design)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

# Game Rules

The game will first greet the player and asks for a username. Then the game begins by randomly generating 5 ships on both the player's and the computer's board. The ships position is marked with the letter "S".

The game will then prompt the player to enter a column and row number of the location they want to target. In case that position holds a battleship, the game will declare a succesful hit and the position is marked with an " * ". If there's  no battleship at the position, it is declared as a miss and is marked with an "x".

The computer's turn is automated and the result is displayed in an identical way to the player's results.

The player and the computer will take ten turns to find all of the ships. In case the 10 turns pass without finding all 5 ships, the game will state who has had the most hits and display them as the winner.

# Features

## Existing features

* Personalised introductory message that states the games rules
* Random generation of ships and boards
* Turn by turn play against the computer
* Target selection by the player
* Turns and scores are tracked to decide the winner
* Input is validated for referencing outside of the grid, entering numbers, duplication

## Planned Features

* Allowing the player to select their ships positions
* Adding decorative features such as ASCII art and colorful text
* Allowing the player to change the level of difficulty by changing the size of the board, number of ships, etc
* Creating additional levels of the game with score tracking and leader board
* The game could include a feature for saving and loading games, allowing players to pick up where they left off at a later time.

# Design

The requirement was to create and deploy a terminal based battleship game in Python programming language.

## Design criteria

* The game should be easy to understand and play for users, with clear instructions provided at the start of the game.
* The game should be visually appealing and easy to navigate, using ASCII art or other similar techniques to display the game board and other relevant information.
* The game should be well-tested and free of bugs or other issues that could negatively impact the player's experience.
* The game should be written in a way that is easy to understand and maintain, with clear and well-documented code.


# Testing

## Validator Testing



# Technologies Used

* GitHub this was  For version control used to host the website, so it is viewable to the public.
* GitPod This was used as an IDE, or the Integrated Development Area.
* PEP8 This was used to check errors and bugs
* Python The game itself is written in python and held in the run.py file.
* Heroku Heroku was used to deploy the website as python is a backend language and the game needed a terminal to display the game.
* Am I Responsive Used to test responsiveness of the game at different screen sizes

# Deployment

* The project was deployed on the Heroku website using Code Institute's terminal template. Here are the steps I have taken to successfully deploy the project: 
    
    1. Create a new repository from the Code Institute Python template.
    2. Create a new Heroku account / Register
    3. Create a new Heroku App
    4. Set the Config Vars to PORT 8000 in the Settings tab
    4. Set buildpacks to Python and NodeJS in this order.
    5. Link the Heroku App into the repository on GitHub
    6. Deploy the App.


# Credits

# Acknowledgements