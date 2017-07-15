# Random Number Guessing Game
# 9 July 2017
# CTI-110 M5HW2 - Random Number Guessing Game
# Terry Goldstrom

import random

# Generate a random number
randomNumber = random.randrange(0,100)
guessed = False

# Get User's guessed number
while guessed==False:
    userInput = int(input("Guess a number between 1 and 100: "))
    # If guessed number equal random number, congradulate user
    if userInput==randomNumber:
        guessed = True
        print("Congratulations, you guessed the number!")
    # Let user know if guessed number is too high
    elif userInput>randomNumber:
        print("Too high, try again")
    # Let user know if guessed number is too low
    elif userInput < randomNumber:
        print("Too low, try again")
