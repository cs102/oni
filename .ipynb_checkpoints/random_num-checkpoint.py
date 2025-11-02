import sys
from termcolor import colored, cprint
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number 1 and {x}: '))
        if guess < random_number:
            cprint('buuu! too low... try again', 'magenta')
        elif guess > random_number:
            cprint('nope! too high... try again', 'light_blue')

    cprint(f'Yay, you did it...the number was {random_number}', 'yellow')

guess(10)
