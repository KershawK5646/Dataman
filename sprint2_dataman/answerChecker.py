# -*- coding: utf-8 -*-
"""
Answer Checker:
    This program will propose to the user a math question and evaluate
    thier answer. If the user enters the correct answer, they will be 
    given praise. If the user enters an incorrect answer, they will be
    instructed to try again until they get it right.

    ## Needs to be updated

"""


import random
import dataManUtil as dmUtil

def answerChecker():
    dmUtil.returnKey()
    print("=======================")
    print("DATAMAN Problem Checker")
    print("=======================")
    progRun = True #Program loop

    while progRun == True:

        print("Let's check your math!")
        print("What kind of problem is it? \n1.+ \n2.- \n3.x \n4.Exit")

        choice = dmUtil.getUserInput()


        if choice == 1:
            doAddProblem()

        elif choice == 2:
            doSubProblem()

        elif choice == 3:
            doMulProblem()

        elif choice == 4:
            progRun = False;

        else:
            print("Enter a valid option!")


def doAddProblem():
    correctAnswer = False
    
    print("\n[] + []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," + []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," + ", num2)

    answer = num1 + num2

    while correctAnswer == False:
        print("What is the answer?")
        checkAnswer = dmUtil.getUserInput()

        if answer == checkAnswer:
              print("\nCorrect! Try another problem!\n")
              correctAnswer = True
        else:
            print("\nIncorrect! Try again!\n")

def doSubProblem():
    correctAnswer = False
    
    print("\n[] - []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," - []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," - ", num2)

    answer = num1 - num2

    while correctAnswer == False:
        print("What is the answer?")
        checkAnswer = dmUtil.getUserInput()

        if answer == checkAnswer:
              print("\nCorrect! Try another problem!\n")
              correctAnswer = True
        else:
            print("\nIncorrect! Try again!\n")

def doMulProblem():
    correctAnswer = False
    
    print("\n[] x []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," x []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," x ", num2)

    answer = num1 * num2

    while correctAnswer == False:
        print("What is the answer?")
        checkAnswer = dmUtil.getUserInput()

        if answer == checkAnswer:
              print("\nCorrect! Try another problem!\n")
              correctAnswer = True
        else:
            print("\nIncorrect! Try again!\n")

            

if __name__ == '__main__':
	answerChecker()    
        

        
