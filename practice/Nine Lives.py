# The Game is called nine lives
import random

lives = 9

words = ['pizza', 'ferry', 'light', 'teeth', 'plane', 'smell']
print('Use these option words:', words)

secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter


while lives > 0:
    print(clue)
    print('lives left:' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word: ')

    if guess == secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print('Incorrect! You loose a life!')
        lives = lives - 1

    if guessed_word_correctly:
        print('You won! The secret word was' + secret_word)
    else:
        print('You lost! The secret word was' + secret_word)
