# BATTLESHIP WARS

Battleship wars is a game that is based on the classic strategy pen and paper game where the 2 players fight for victory 
by destroying each other's ships. This version of the game is a python based game played via the terminal inside a code 
editor, or in this case this game is deployed on Heroku which creates a terminal to play on.

Players will be playing against a computer that will try to find all the players ships before they do, 
the first to lose all of his ships loses the game. There are 4 ships in total with 4 different sizes going from 
a ship that occupies 2 rows/columns to a ship that occupies 5.

## How to play

Inside the terminal the first thing the player will see is how to play the game. Here it explains 
what all different symbols mean. The players ships are indicated with a *, the empty spots are indicated with [ ], 
the misses with o and the hits with an X. In turns the player and computer get a shot at each other, the player
chooses his/hers shots by typing in the coordinates (example: B5/h7) The first who sinks all the opponents ships
wins the game and can after enter 'y' to go again or 'n' to stop playing.

## Features

### Existing features

- Battlefield

    - Both the players boards are generated randomly making sure the ships stay inside the grid and don's overlap each other
    - The player is unable to see the opponents ships

- The opponent
    - The player is going against a computer
    - The computer does not strike more than once in the same spot
    - The computer if it gets one hit it will try to find the second one otherwise it will start looking at different places again

- Feedback and error messages
    - The player gets a feedback after every round if he/her got shot or if the computer missed
    - The player also gets a feedback if he/she gets a got or miss on the opponents grid
    - If invalid coordinates are given larger than the grid itself it displays an error message


### Future features

- Ship placement
    - The player can decide where he/she wants to put the ships on the grid

- Opponent
    - A smarter opponent that if it finds a ship it will continue to fire on it until it's gone completely 

## Data model

A two dimensional array was used for the grid to store the current state. Here there are 4 different states used which 
are the water state which if tried to hit changes to the mis state and the boat state which if hit changes to hit state.

## Testing 

### Self testing

- I player the game multiple times to see if everything works correctly
- I tried giving wrong inputs to see if I get an error messages when I enter
  a wrong coordinate or I type in just one letter or number
- I tested if the 'y' and 'n' function works at the end and if it resets the game
- The code was also tested inside the terminal on the Heroku app

### Validator Testing 

I ran the code through the PEP8 validator. No errors returned.

## Bugs

### Known Bugs

- I was unable to find any bugs in the end result

## Deployment

- The following steps have to be
    - Open Heroku
    - Create a new app in Heroku
    - Go to settings inside the created app
    - Click on add buildpack and add Python first and then NodeJS
    - Now click on config vars and add one with PORT as a key and 8000 as the value
    - Go to deploy and connect your GitHub account
    - Under that link the repository to Heroku
    - At the bottom of the page click the deploy branch button