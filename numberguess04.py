#!/usr/bin/env python3

# Number Guess - guess a number between 1 and 100 in 5 tries
# Jason Culligan
# 06/08/2018

# import sys
import os
import random

used = []
tries = 5
max = 100
number = random.randrange(1, max)


def lose():
    print("Hard luck!  The number I was thinking of was", number, "!")
    exit()


def win():
    print("You Win!")
    exit()


os.system('cls' if os.name == 'nt' else 'clear')
print("I'm thinking of a number between 1 and", max)
print("See if you can guess it in 5 tries.")
print("")

while tries != 0:
    if tries < 5:
        print("You have", tries, "tries left.")
    guess = int(input("Your guess: "))
    os.system('cls' if os.name == 'nt' else 'clear')

    if guess == number:
        print("You Win!")
        exit()

    if guess in used:
        print("You already used that number.  Try a different number")
        tries += 1
    else:
        if guess <= max:
            used.append(guess)

    if guess < number:
        tries -= 1
        if tries == 0:
            lose()
        if tries != 0:
            print(guess, "is too low, guess higher")
            # tries -= 1

    if guess > number:
        if guess < max:
            tries -= 1
            if tries == 0:
                lose()
            else:
                print(guess, "is too high, guess lower")
        if guess > max:
            print("Aw come on!  That's way too high!")
