# project on a game called guess the animal

import time


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 4:
        if guess.casefold() == answer.casefold():
            print('Correct answer!')
            score = score + 10
            still_guessing = False

        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again: ')
            attempt = attempt + 1

        if attempt == 3:
            guess = input('Sorry wrong answer. You have one more chance left!: ')
            attempt = attempt + 1

        if attempt == 4:
            print('The correct answer is  ' + answer)


score = 0
print('Guess The Animal!')
guess_1 = input("Which animal lives in the North Pole?\n A) Whale \n B) Polar Bear \n C) Fish \n Type Answer A, "
                "B or C: ")
check_guess(guess_1, 'B')
time.sleep(1.25)
print()

guess_2 = input("Which would you call a group of fishes?\n A) A school \n B) An army \n C) A collection \n Type "
                "Answer A, B or C: ")
check_guess(guess_2, 'A')
time.sleep(1.25)
print()

guess_3 = input("Fish don't have lungs, instead they breathe through?\n A) Dorsal fins \n B) Scales \n C) Gills \n Type"
                "Answer A, B or C: ")
check_guess(guess_3, 'C')
time.sleep(1.25)
print()

guess_4 = input("Which species of fish is Nemo in the 2003 film, 'Finding Nemo'?\n A) Clownfish \n B) Rasbora \n C) "
                "Angelfish \n Type Answer A, B or C: ")
check_guess(guess_4, 'A')
time.sleep(1.25)
print()

guess_5 = input("When do porcupine-fish inflate their bodies into a round shape by sucking water?\n A) When they have "
                "sex \n B) When they digest food)"
                "\n C) When they Face dangers \n Type Answer A, B or C: ")
check_guess(guess_5, 'C')
time.sleep(1.25)
print()

guess_6 = input("Which of the following is NOT a reason why fish have colourful patterns on the skins?\n A) To make "
                "them easier to catch \n"
                "B) To attract mates \n C) To hide them form predators \n Type Answer A, B or C: ")
check_guess(guess_6, 'A')
time.sleep(1.25)
print()

guess_7 = input("Which is the biggest fish in the world?\n A) Whale Shark \n B) Ocean sunfish \n C) Beluga Sturgeon "
                "\n Type Answer A,"
                "B or C: ")
check_guess(guess_7, 'A')
time.sleep(1.25)
print()

guess_8 = input("The ocean sunfish is known for producing more eggs than other vertebrates. Approximately how many "
                "can they produce at a time?\n A) 3000 \n B) 300000000 \n C) 300000 \n Type Answer A, B or C: ")
check_guess(guess_8, 'B')
time.sleep(1.25)
print()

guess_9 = input("Which Country is the biggest salmon producer in the world?\n A) China \n B) Norway \n C) Chile \n "
                "Type Answer A, B or C: ")
check_guess(guess_9, 'B')
time.sleep(1.25)
print()

guess_10 = input("What health issue would happen when you eat puffer fish?\n A) Increased blood pressure \n B) Food "
                 "poisoning \n C) Diabetes \n Type Answer A, B or C: ")
check_guess(guess_10, 'B')
time.sleep(1.25)
print()

guess_11 = input("What is the gender of all clownfish when they are born?\n A) Male \n B) Female \n C) Unisex \n Type "
                 "Answer A, B or C: ")
check_guess(guess_11, 'A')
time.sleep(1.25)
print()

guess_12 = input("What is the name of the branch of science devoted to studying fish? \n A) Anthropology \n "
                 "B) Ornithology \n C) Ichthyology \n Type Answer A, B or C: ")
check_guess(guess_12, 'C')
time.sleep(1.25)
print()

guess_13 = input("The ocean sunfish is known for producing more eggs than other vertebrates. Approximately how many "
                 "can they produce at a time?\n A) 3000 \n B) 300000000 \n C) 300000 \n Type Answer A, B or C: ")
check_guess(guess_13, 'A')
time.sleep(1.25)
print()

guess_14 = input("Most of the species of goldfish belong to which fish of family?\n A) Herring family \n B) Carp "
                 "Family \n C) Beta fish family \n Type Answer A, B or C: ")
check_guess(guess_14, 'B')
time.sleep(1.25)
print()

print('Your score is....')
time.sleep(2)
print(str(score))
