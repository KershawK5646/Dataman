# -*- coding: utf-8 -*-
"""
Dataman Calculator:
    This program is an ordinary calculator that will prompt the user to
    enter a type of problem, ask for the user to enter two numbers, and
    then solve the problem while displaying the answer to them.
    
"""


import random
import dataManUtil as dmUtil

def datamanCalculator():
    print("DATAMAN Calculator")
    progRun = True #Program loop

    while progRun == True:

        print("Let's do some math!")
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

    answer = num1 + num2

    print("\n", num1," + ", num2, " = ", answer, "\n")

def doSubProblem():
    correctAnswer = False
    
    print("\n[] - []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," - []")
    num2 = dmUtil.getUserInput()

    answer = num1 - num2

    print("\n", num1," - ", num2, " = ", answer, "\n")


def doMulProblem():
    correctAnswer = False
    
    print("\n[] x []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," x []")
    num2 = dmUtil.getUserInput()

    answer = num1 * num2

    print("\n", num1," x ", num2, " = ", answer, "\n")

         

if __name__ == '__main__':
	datamanCalculator()    
        

        
