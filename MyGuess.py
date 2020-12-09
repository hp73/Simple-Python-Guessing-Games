"""
Author: Harry Pinkerton
Project 3
File: MyGuess.py

This program plays a guessing game with the user.  The program
displays a greeting and thinks of a number between 1 and 100.
The user inputs guesses until a guess equals the number. If user's
guess is too large or too small, the computer replies with a hint
to that effect.  When the user guess the number, the program displays
the total number of guesses.  
"""

import random
import math

myNumber = random.randint(1, 100)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if count > math.log(100,2) +1:
        print("Too many attempts! You Lose!")
        break
    elif userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("You've got it in", count, "tries!")
        break
