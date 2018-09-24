import random

secretNumber = random.randint(1, 100)
print('I am thinking of a number between 1 and 100.')

for guessesTaken in range(1, 11):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Nice.  You guessed my number in', str(guessesTaken), 'guesses.')
else:
    print('You suck.  The number I was thinking was ', str(secretNumber))
