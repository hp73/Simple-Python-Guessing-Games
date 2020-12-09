"""
Author: Harry Pinkerton
Project 3
File: YourGuess.py

This program plays a guessing game with the computer. The program guesses until
it gets the user's number correct using hints from the user whether or not the
computer's guess is too large or too small. When the computer guesses the number
the program displays the total number of guesses.  
"""

import random
import math
lowerBound = 0
upperBound = 100

count = 0
while True:
    count += 1
    compNumber = (lowerBound + upperBound) // 2
    print("Is this your number",compNumber) 
    userNumber = str(input("Enter your hint, too small, too large, or correct: "))
    if count > math.log(100,2) +1:
        print("Too many attempts! You Lose!")
        break
    elif userNumber == "too small":
        lowerBound = compNumber
    elif userNumber == "too large":
        upperBound = compNumber
    elif userNumber == "correct":
        print ("Yay! I got it in", count, "tries!")
        break
    else:
        print("Invalid Input, Try Again")
   
