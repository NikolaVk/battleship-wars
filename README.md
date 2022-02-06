# BATTLESHIP WARS

Battleship wars is a game that is based on the classic strategy pen and paper game where the 2 players fight for victory 
by destroying each other's ships. This version of the game is a python based game played via the terminal inside a code 
editor, or in this case this game is deployed on Heroku which creates a terminal to play on.

Players will be playing against a computer that will try to find all the players ships before they do, 
the first to lose all of his ships loses the game. There are 4 ships in total with 4 different sizes going from 
a ship that occupies 2 rows/columns to a ship that occupies 5.

I created this game because I always enjoy playing this type of game as a board version. 

[Here you can find the live version of my project](https://battleship-wars.herokuapp.com/)

<img src="https://github.com/NikolaVk/battleship-wars/blob/master/images/startpoint.png">

## Table of contents
1. [How to play](#Howtoplay)
2. [UX](#UX)
3. [Features](#Features)
4. [Technologies Used](#Technologies)
5. [Testing](#Testing)
6. [Deployment](#Deployment)
7. [Credits](#Credits)

## How to play

Inside the terminal the first thing the player will see is how to play the game. Here it explains 
what all different symbols mean. The players ships are indicated with a *, the empty spots are indicated with [ ], 
the misses with o and the hits with an X. In turns the player and computer get a shot at each other, the player
chooses his/hers shots by typing in the coordinates (example: B5/h7) The first who sinks all the opponents ships
wins the game and can after enter 'y' to go again or 'n' to stop playing.

## UX

### Visitor stories

    - As a visitor of "Battleship Wars" I want/need

    1. An explenation of how the game works.
    2. Clear instructions on how to play
    3. For the game to let me know if I did something wrong
    4. To be able to quit the game when I want
    5. After the game is finished to be able to restart the game widouth refreshing the site

## Features

### Existing features

- Battlefield

    - Both the players boards are generated randomly making sure the ships stay inside the grid and don's overlap each other
    - The player is unable to see the opponents ships

<img src="https://github.com/NikolaVk/battleship-wars/blob/master/images/grids.png">

- The opponent
    - The player is going against a computer
    - The computer does not strike more than once in the same spot
    - The computer if it gets one hit it will try to find the second one otherwise it will start looking at different places again

- Feedback and error messages
    - The player gets a feedback after every round if he/her got shot or if the computer missed
    - The player also gets a feedback if he/she gets a got or miss on the opponents grid
    - If invalid coordinates are given larger than the grid itself it displays an error message

<img src="https://github.com/NikolaVk/battleship-wars/blob/master/images/errormsg.png">


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

<img src="https://github.com/NikolaVk/battleship-wars/blob/master/images/validator.png">

## Bugs

### Known Bugs

- I was unable to find any bugs in the end result

- ## Technologies used

    - ### Languages used
        
        - [HTML](https://en.wikipedia.org/wiki/HTML)
        - [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
        - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

    - ### Frameworks, libraries and programs used

        - [Heroku](https://dashboard.heroku.com) was used to host the app
        - [Random](https://docs.python.org/3/library/random.htmlhttps://docs.python.org/3/library/random.html) was used to position the ships randomly across the board
        - [sys](https://docs.python.org/3/library/sys.html) was used by the sys.exit function to exit the application
        - [JQuery](https://jquery.com/) Was already inside the CI templade
        - [XTERM](https://github.com/xtermjs/xterm.js#readme) Was already inside the CI templade
        - [PEP8 Validator](http://pep8online.com/) Was used to test the code for errors

    - ### Tools

        - [Git](https://nl.wikipedia.org/wiki/Git_(software)) and - [Github](https://www.gitpod.io/docs)  Was used to handle version control and store my code
        - [Gitpod](https://www.gitpod.io/docs) was used as my IDE


- ## Deployment

This project was made using Gitpod and Github. This project has some secure information which is why an run.py file was used

- ### Instructions Making a Local Clone

    1. Make an account or login to Github and go to the main page of the repository[link](https://github.com/NikolaVk/battleship-wars)
    2. Above all the files besides the large green Gitpod button click on code.
    3. Now copy the link unter the HTTPS tab
    4. Open whatever code editor you use
    5. Open a new work directory or opan an existing one
    6. In the terminal type in git clone and then paste the url you copied behind it and click enter


- ## Deploying this project to Heroku

    1. Create an account on Herouk or login
    2. Create a new app within Heroku
    3. Set the region you are in or otherwiae the closest one to you
    4. After doing all that go to the settings bar and click on "Reveal Config Vars" and type in:

    <pre>
    Config Vars
    KEY: PORT   VALUE: 8000
    </pre>

    6. Now add, commit and push to Github
    7. After doing that return to heroku and click on the deploy tab and chose Github as deployment method
    8. Now connect your repository name after that is ready
    9. Scroll down and click "enable automatic deployment"
    10. Click deploy and your ready to go

- ## Credits 

    - ### Code

    - ### Acknowledgements