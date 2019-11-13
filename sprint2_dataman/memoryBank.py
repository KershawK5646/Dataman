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

def memoryBank(cards):
    print("")
    print("===================")
    print("DATAMAN Memory Bank")
    print("===================")
    print("\n1. Create Deck \n2. Study \n3. Empty Deck\n4. Exit")
    choice = dmUtil.getUserInput()

    if choice == 1:
        createCards(cards)
    elif choice == 2:
        useCards(cards)
    elif choice == 3:
        deleteCards(cards)
    elif choice == 4:
        print()
        print("Exiting...")
    else:
        print()
        print("Invalid option. Try again.")
        memoryBank(cards)

def createCards(cards):
    # creates .csv file 'deck' of cards
    print()
    print("Let's make some flashcards.")
    print("How many cards?")
    count = dmUtil.getUserInput()
    print()
    cardChoice(count, cards)
    json.dump(cards, open('cards.csv','w'))
    print(f"Your deck so far: {cards}") # visual verification of cards
    memoryBank(cards)

def cardChoice(count, cards):
    for i in range(count):
        print("For this card, choose an operator: \n1. + \n2. - \n3. *")
        choice = dmUtil.getUserInput()
        print(f"Choice was {choice}")

        if choice == 1:
            add(cards)
            i += i
        elif choice == 2:
            sub(cards)
            i += i
        elif choice == 3:
            mul(cards)
            i += i
        else:
            print()
            print("Invalid option. Try again.")
            cardChoice(count, cards)

def add(cards):
    print("\n[] + []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," + []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," + ", num2)
    problem = f"{num1}+{num2}"
    answer = num1 + num2
    cards[problem] = str(answer)
    return cards

def sub(cards):
    print("\n[] - []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," - []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," - ", num2)
    problem = f"{num1}-{num2}"
    answer = num1 - num2
    cards[problem] = str(answer)
    return cards    

def mul(cards):
    print("\n[] * []")
    num1 = dmUtil.getUserInput()
    print("\n", num1," * []")
    num2 = dmUtil.getUserInput()
    print("\n", num1," * ", num2)
    problem = f"{num1}*{num2}"
    answer = num1 * num2
    cards[problem] = str(answer)
    return cards

def useCards(cards):
    # user is given previously input math problems
    # and their score
    cards = json.load(open('cards.csv','r'))
    correct = 0
    incorrect = 0
    total = 0
    print()
    print("Ready? Go!")
    
    for key in cards:
        print(key)
        print("Answer: ")
        guess = dmUtil.getUserInput()

        if str(guess) == cards[key]:
            print()
            print("Correct!")
            correct += 1
            total += 1
        else:
            print()
            print("Incorrect!")
            incorrect += 1
            total += 1

    if total > 0:        
        score = (correct / total) * 100
        print()
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

    else:
        print()
        print("You can't study an empty deck!")
        print("Use Create Deck to get started!")

    again()

def again():
    print("Would you like to study the same cards again?")
    print("\n1. Yes \n2. No")
    choice = dmUtil.getUserInput()
    
    if choice == 1:
        useCards(cards)
    elif choice == 2:
        print("Returning...")
        memoryBank(cards)
    else:
        print()
        print("Invalid option. Try again.")

def deleteCards(cards):
    print("Are you sure you want to empty your deck?")
    print("THIS CANNOT BE UNDONE!")
    print("\n1. Yes \n2. No")
    choice = dmUtil.getUserInput()
    if choice == 1:
        cards = {}
        json.dump(cards, open('cards.csv','w'))
        memoryBank(cards)
    elif choice == 2:
        print("Whew... close one.")
        memoryBank(cards)
    else:
        print()
        print("Invalid option. Try again.")
        
if __name__ == '__main__':
    memoryBank(cards)
