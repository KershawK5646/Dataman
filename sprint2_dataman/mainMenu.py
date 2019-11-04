# -*- coding: utf-8 -*-
"""
Dataman Menu:
    
    This program will act as the main driver class as well as the main menu for
    our dataman project.
"""

# Imports
import dataManUtil as dmUtil
import answerChecker
import popQuiz
import guessTheNumber
import datamanCalculator
import memoryBank

# Intro
def intro():
    # This introduces the program to the user.
    print("=================")
    print("=====DATAMAN=====")
    print("=================")
    print("\n")
    
# Selection
def selection():
    # This displays the users options to them.
    print("Please make a selection from the following: ")
    print("1. Answer Checker. \n2. Pop Quiz. \n3. Guess the Number. \n4. Memory Bank. \n5. Calculator. \n6. Exit.")    

# Main
def main():
    goAgain = True
    
    # Loop to keep user in program.
    while goAgain == True:
        # Call the intro
        intro()
        selection()
        
        # Get user menu selection
        menuSelection = dmUtil.getUserInput()

        while menuSelection >6 or menuSelection <1:
            print("Entered number out of bounds. Please enter a number within range.")
            selection()
            menuSelection = dmUtil.getUserInput()
        
        if menuSelection == 1:
            # AnswerChecker
            answerChecker.answerChecker()
        if menuSelection == 2:
            # Pop Quiz
            popQuiz.popQuiz()
        if menuSelection == 3:
            # Guess the Number
            guessTheNumber.guessTheNumberGame()
        if menuSelection == 4:
            #Memory bank
            memoryBank.memoryBank()
        if menuSelection == 5:
            # Dataman Calculator
            datamanCalculator.datamanCalculator()
        if menuSelection == 6:
            # Exits the program
            print("Goodbye!")
            break          
        
        # Ask the user if they want to repeat the program
        goAgain = dmUtil.goAgain()

if __name__ == '__main__':
	main()
