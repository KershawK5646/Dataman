# -*- coding: utf-8 -*-
"""
PopQuiz:
    This program will store a series of previously entered math problems
    for the user to practice with. This will function similarly to 
    flash-cards.
"""
# Imports
import dataManUtil as dmUtil
import random

# Main loop
def popQuiz():
    # Bool to control game state
    gameLoop = True
    print("DATAMAN Pop Quiz")
    while gameLoop = True:
        # Generatr randoms needed for numbers and operator
        number1 = getRandomNumber()
        number2 = getRandomNumber()
        operator = getRandomOperator()
        
        # Propose the question
        #questionPropt(number1 + " " + operator + " " number2 + "= :")
        
        #print(questionPrompt)
        
        # Go again question
        gameLoop = again()
    
# Generate and return a random number
def getRandomNumber():
    randomNumber = randint(0,10)
    print(randomNumber)
    return randomNumber

# Use a random number to get a random operator
def getRandomOperator():
    operatorSelection = randint(0,2)
    print(operatorSelector)
    
# Go again function
def again():
    print("Would you like to study the same cards again?")
    print("\n1. Yes \n2. No")
    choice = dmUtil.getUserInput()
    
    # Repeat selection
    if choice == 1:
        return True
    # Quit selection
    elif choice == 2:
        return False

if __name__ == '__main__':
    popQuiz()