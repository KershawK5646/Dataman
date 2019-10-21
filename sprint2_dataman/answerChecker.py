# -*- coding: utf-8 -*-
"""
Answer Checker:
    This program will propose to the user a math question and evaluate
    thier answer. If the user enters the correct answer, they will be 
    given praise. If the user enters an incorrect answer, they will be
    instructed to try again until they get it right.

"""


import random
import dataManUtil as dmUtil

def answerChecker():
    print("DATAMAN Problem Checker")

    problemRange = 10 #Sets a range for the numbers involved in the problems
    solved = 0 #Counter for correct answers
    progRun = True #Keeps the program running
    
    num1 = random.randint(0,problemRange) #First number in the problem
    num2 = random.randint(0,problemRange) #Second number in the problem

    while progRun == True: 

        correctAnswer = False #Checks if problem was solved right

        problemType = random.randint(1,3) #Rolls a number that will determine the problem type

        if problemType == 1:
            solution = num1 + num2
            print(num1," + ",num2," = ? ")  
            
        elif problemType == 2:
            solution = num1 - num2
            print(num1," - ",num2," = ? ")
            
        else:
            solution = num1 * num2
            print(num1," x ",num2," = ? ")

        while correctAnswer == False:
            print("What is the answer? \n[101: Skip problem | 102: Exit] ");
            choice = dmUtil.getUserInput()            
            
            if choice == solution:
                solved+=1
                print("Correct! You have answered",solved,"problems correctly!")
                print("Goodjob!\n")
                correctAnswer = True
                
            elif choice == 101:
                print("Skipped! Correct answers reset.\n")
                solved = 0
                correctAnswer = True 
                
            elif choice == 102:
                correctAnswer = True
                progRun = False
                
            elif choice != solution:
                print("Incorrect! Try again.\n")    
 
        num1 = random.randint(1,problemRange)
        num2 = random.randint(1,problemRange)

if __name__ == '__main__':
	answerChecker()    

