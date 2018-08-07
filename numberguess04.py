#!/usr/bin/env python3

# Number Guess - guess a number in 5 tries.  Range based on selected difficulty
# Jason Culligan
# 07/08/2018

# import sys
import os
import random

used = []
tries = 5
max = 0



def lose():
    print("Hard luck!  The number I was thinking of was", number)
    print("")
    exit()


def win():
    print("You Win!")
    print("")
    exit()


os.system('cls' if os.name == 'nt' else 'clear')

print("Select difficulty by entering the number")
print(" Easy - 1")
print(" Medium - 2")
print(" Hard - 3")
print(" Insane - 4")

while True:
    difficulty = input("?: ")
    if difficulty not in ('1', '2', '3', '4'):
        print("Pick between 1 and 4 please")
    else:
        break

if difficulty == "1":
    max = 10
if difficulty == "2":
    max = 100
if difficulty == "3":
    max = 500
if difficulty == "4":
    max = 1000


number = random.randrange(1, max)
os.system('cls' if os.name == 'nt' else 'clear')

print("I'm thinking of a number between 1 and", max)
print("See if you can guess it in 5 tries.")
print("")

while tries != 0:
    if tries < 5:
        print("You have", tries, "tries left.")
    while True:
        try:
            guess = int(input("Your guess: "))
            break
        except:
            print("Numbers only please!")

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
        if guess >= 1:
            tries -= 1
            if tries == 0:
                lose()
            if tries != 0:
                print(guess, "is too low, guess higher")
        if guess < 1:
            print("Aw come on!  That's way too low!")

    if guess > number:
        if guess <= max:
            tries -= 1
            if tries == 0:
                lose()
            else:
                print(guess, "is too high, guess lower")
        if guess > max:
            print("Aw come on!  That's way too high!")
