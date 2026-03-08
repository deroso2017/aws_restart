# Use a while loop
# Use a for loop

import random

number = random.randint(1, 10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# Loop from 0 up to (but not including) 11
for x in range(0, 11):  # generate list from 0 to 10
    print(x)
