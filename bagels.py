# Bagels, a deductive logic game where 
# you must guess 
# a number based
# clues.

import random

num_digits = 3
max_guess = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:
That means:
Pico
One digit is correct but in the wrong position.
Fermi
One digit is correct and in the right position.
Bagels
No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(num_digits))
    
    while True:
        secretNum = getSecretNum()
        print("I have thought up a number")
        print("You have {} guesses to get it.".format(max_guess))

        numGuesses = 1
        while numGuesses <= max_guess:
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print("Guess #{}".format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guess:
                print("You ran out of guesses")
                print('The answer was {}'.format(secretNum))

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
    print('Thanks for playing')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bargels'
    else:
        clues.sort()
        return ''.join(clues)

if __name__ == '__main__':
    main()