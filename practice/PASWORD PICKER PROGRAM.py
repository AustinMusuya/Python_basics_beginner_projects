import string
import random

print("Welcome to Password Picker")

while True:
    adjectives = ['sleepy', 'slow', 'smelly', 'white', 'proud', 'brave'
                                                                'wet', 'fat', 'red', 'orange', 'yellow', 'green',
                  'purple']

    nouns = ['apple', 'dinosaur', 'panda', 'toaster', 'baller', 'dragon', 'duck', 'hammer']

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    
    special_character = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_character

    response = input('Would you like a new password? Type yes/no:')

    if response.casefold() == 'yes':
        print(f'Your new password is: {password}')
    elif response.casefold() == 'no':
        break
    else:
        print("Kindly choose valid option:\n yes/no")
