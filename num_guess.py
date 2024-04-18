# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/17/2024
# Description: try to guess for an integer
import random
def num_guess():
        target = int(input("Enter the integer for the player to guess."))
        guess = None
        tries = 0
        print("Enter your guess.")
        while guess != target:
            guess = int(input())
            tries += 1
            if guess > target:
                print("Too high - try again:")
            elif guess < target:
                print("Too low - try again:")
            else:
                print(f"You guessed it in {tries} tries.")
num_guess()
