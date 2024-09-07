# A simple guessing game using while loop and if statements

import random

guess = 0
random_number = random.randrange(1,11)
while guess != random_number:
    guess = int(input("Try to guess your number:"))
    if guess == random_number:
        print('You got it right')
    elif guess > random_number:
        print('Number to high, try a lower number')
    elif guess < random_number:
        print('Number is too low, try a higher number')