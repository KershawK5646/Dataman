# -*- coding: utf-8 -*-
"""
dataManUtility:
    This file will hold utility functions used across all other files
    within this assignment.
"""

def getUserInput():
    while True:
        try:
            userInput = int(input("Please enter a number: "))
            return userInput
        except ValueError:
            print("That was not a number. Please enter a number.")
            
def goAgain():
    print("Would you like to go again? \n1. Yes \n2. No")
    goAgainAnswer = getUserInput()
    
    while goAgainAnswer >2 or goAgainAnswer <1:
        print("That selection was out of bounds. Please select either 1 or 2.")
        goAgainAnswer = getUserInput()
    
    if goAgainAnswer == 1:
        print("Going again!")
        goAgain = True
        return goAgain
    elif goAgainAnswer == 2:
        print("Goodbye!")
        goAgain = False
        return goAgain