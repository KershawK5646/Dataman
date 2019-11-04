# -*- coding: utf-8 -*-
"""
MemoryBank:
    This program will store a series of previously entered math problems
    for the user to practice with. This will function similarly to 
    flash-cards.
"""

import json
import dataManUtil as dmUtil
cards = {}

def memoryBank():
    print("DATAMAN Memory Bank")
    print("\n1. Create \n2. Study \n3. Exit")
    choice = dmUtil.getUserInput()
    if choice == 1:
        createCards(cards)
    elif choice == 2:
        print("UNDER CONSTRUCTION!!! \nComing soon...")
        # useCards(cards)
        memoryBank()
    elif choice == 3:
        print("Returning...")
    else:
        print("Invalid option. Try again.")
        memoryBank()

def createCards(cards):
    # creates .csv file 'deck' of cards
    print("Let's make some flashcards.")
    print("How many cards?")
    count = dmUtil.getUserInput()
    cardChoice(count, cards)
    json.dump(cards, open('cards.csv','w'))
    print(cards) # visual verification of cards
    memoryBank()

def cardChoice(count, cards):
    for i in range(count):
        print("For this card, choose an operator: \n1. + \n2. - \n3. *")
        choice = dmUtil.getUserInput()
        if choice == 1:
            add(cards)
            i += i
        elif choice == 2:
            sub()
            i += i
        elif choice == 3:
            mul()
            i += i
        else:
            print("Invalid option. Try again.")
            cardChoice(count, cards)

def add(cards):
    print("\n[] + []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," + []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," + ", num2)
    problem = "{0}+{1}".format(num1, num2)
    answer = num1 + num2
    cards[problem] = answer
    return cards

def sub():
    print("\n[] - []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," - []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," - ", num2)
    answer = num1 - num2

def mul():
    print("\n[] * []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," * []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," * ", num2)
    answer = num1 * num2

def useCards(cards):
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

    again()

def again():
    print("Would you like to study the same cards again?")
    print("\n1. Yes \n2. No")
    choice = dmUtil.getUserInput()
    
    if choice == 1:
        useCards()
    elif choice == 2:
        print("Returning...")
        memoryBank()
        
if __name__ == '__main__':
    memoryBank()