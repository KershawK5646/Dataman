# -*- coding: utf-8 -*-
"""
Guess the Number:
    This program will choose a number between a range and isntruct the user
    to guess it. The program will help the user dial in with tips like
    "Too low" or "Too high" based on their input until they guess the 
    correct number. It will also keep track of how many times the user 
    had to guess and will display this to the user once finished.
"""

import random
import dataManUtil as dmUtil

def guessTheNumberGame():
    # Create random number
    randomNumber = random.randint(1,100)
    # Create a counter for the number of guesses.
    guessCounter = 0
    # Create a bool for gameover status.
    gameOver = False
    print("I'm thinking of a number...between 1 and 100....Take a guess!")
    
    # Create loop using bool to control it.
    while gameOver == False:
        # Get a guess from the user.
        userNumber = dmUtil.getUserInput()
        # Add one to the counter.
        guessCounter = guessCounter + 1
        
        # Evaluate the user guess.
        if userNumber > randomNumber:
            print("Too high... Try again!")
        elif userNumber < randomNumber:
            print("Too Low... Try again!")
        else:
            print("That's right! You guessed ", randomNumber, "in only ",
                  guessCounter, "tries!")
            # Set the game over controller to end the loop
            gameOver = True
        


    