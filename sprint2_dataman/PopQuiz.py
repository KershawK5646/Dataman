# -*- coding: utf-8 -*-
"""
PopQuiz:
    This program will store a series of previously entered math problems
    for the user to practice with. This will function similarly to 
    flash-cards.
"""

import json
import dataManUtil as dmUtil

def memoryBank():
    print("DATAMAN Pop Quiz")
    print("\n1. Create \n2. Study")
    choice = dmUtil.getUserInput()
    if choice == 1:
        createCards()
    elif choice == 2:
        useCards()
    else:
        print("Invalid option. Try again.")
        memoryBank()

def createCards():
    # create array of user input math problems
    # for user to solve
    print("Let's make some flashcards.")
    print("How many cards?")
    count = dmUtil.getUserInput()
    # number of flashcards is set given by user
    print("Type the problem, hit the spacebar, type the answer, and then hit enter.")
    cards = dict(input().split() for _ in range(count))
    # this creates a dictionary using user input
    # user can input problem, then a space, and then the correct answer
    # example: '2+2' ``space key`` '4'
    # this will be put into dictionary with '2+2' as the key
    # and '4' will be the value
    json.dump(cards, open('cards.csv','w'))
    print(cards) # for now, this verifies the user made the cards correctly
    memoryBank()

def useCards():
    # user is given previously input math problems
    # and their score
    cards = json.load(open('cards.csv','r'))
    correct = 0
    incorrect = 0
    total = 0
    print("Ready? Go!")
    for key in cards:
        print(key)
        print("Answer: ")
        guess = dmUtil.getUserInput()
        if str(guess) == cards[key]:
            print("Correct!")
            correct += 1
            total += 1
        else:
            print("Incorrect!")
            incorrect += 1
            total += 1
    score = (correct / total) * 100
    print("Correct: ",correct,"Incorrect: ",incorrect)
    if score > 90:
        print("Great job!")
        print("Score:",score,'%')
    elif score > 80:
        print("Good job!")
        print("Score:",score,'%')
    elif score > 60:
        print("Keep it up!")
        print("Score:",score,'%')
    else:
        print("Better luck next time!")
        print("Score:",score,'%')
        
if __name__ == '__main__':
    memoryBank()
