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
    dmUtil.returnKey()
    # Bool to control game state
    gameLoop = True
    print("================")
    print("DATAMAN Pop Quiz")
    print("================")
    while gameLoop == True:
        # Generatr randoms needed for numbers and operator
        number1 = getRandomNumber()
        number2 = getRandomNumber()
        operator = getRandomOperator()
        
        # Assign string values for operator
        if operator == 0:
            operatorChar = "+"
            questionPrompt = str(number1)+" "+operatorChar+" "+str(number2)+" = "
            answer = number1 + number2
        
        elif operator == 1:
            operatorChar = "-"
            questionPrompt = str(number1)+" "+operatorChar+" "+str(number2)+" = "
            answer = number1 - number2
        
        else:
            operatorChar = "X"
            questionPrompt = str(number1)+" "+operatorChar+" "+str(number2)+" = "
            answer = number1 * number2

        
        
        print(questionPrompt)
        userAnswer = dmUtil.getUserInput()
        while userAnswer != answer:
            print("Not quite...Try again!")
            print(questionPrompt)
            userAnswer = dmUtil.getUserInput()
            
        dmUtil.returnKey()
        print("That's right!")
        print(questionPrompt, answer)

        
        # Go again question
        gameLoop = again()
    
# Generate and return a random number
def getRandomNumber():
    randomNumber = random.randint(0,10)
    # Test print
    #print(randomNumber)
    return randomNumber

# Use a random number to get a random operator
def getRandomOperator():
    operatorSelection = random.randint(0,2)
    # Test print
    # print(operatorSelection)
    return operatorSelection
    
    
# Go again function
def again():
    print("\nWould you like to do another one?")
    print("1. Yes \n2. No")
    choice = dmUtil.getUserInput()
    dmUtil.returnKey()
    
    # Repeat selection
    if choice == 1:
        return True
    # Quit selection
    elif choice == 2:
        return False
    

if __name__ == '__main__':
    popQuiz()
