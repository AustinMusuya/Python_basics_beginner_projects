# Project ATM Functionality
# National bank Atm Project

import time
# this imports the time command so that
# we can make the code wait a specific time frame before doing something.

import sys

# this imports system commands

user_balance = 100000
# setting the user balance to work with
trans1 = 'NA'
trans2 = 'NA'
trans3 = 'NA'
trans4 = 'NA'
trans5 = 'NA'
trans6 = 'NA'
trans7 = 'NA'
trans8 = 'NA'
trans9 = 'NA'
trans10 = 'NA'
'''
the trans are for when the user inputs a value,
it changes the value of trans1 to what you withdrew or deposited
'''
time.sleep(0.75)
# this makes it so the code waits for 0.75  secs
print('''PS the PIN code is 4796.
Don't use caps.
You can only see your previous 10 transactions.''')
time.sleep(1)
print('Welcome to National Bank ATM System')
print()
time.sleep(1)
attempts = True
# creates a variable called attempts
# and sets its value to True for the loops to be created.
while attempts:
    # A loop is created for whenever attempts is true, it keeps going
    attempt_1 = input('Please Enter Pin: ')
    if attempt_1 == '4796':
        # 'if statement' checks if user entered the correct pin.
        print('Correct Pin')
        time.sleep(1)
        break
        # because the user entered the correct pin,
        # the loop will break, and so the code continues.
    else:
        print('Incorrect Pin')
        time.sleep(0.75)
        attempt_2 = input('Please Enter Pin: ')
        if attempt_2 == '4796':
            # 'if statement' checks if user entered the correct pin.
            print('Correct Pin')
            time.sleep(1)
            break
        else:
            print('Incorrect Pin')
            time.sleep(0.75)
            print('You have one more attempt')
            attempt_3 = input('Please Enter Pin: ')
            if attempt_3 == '4796':
                # 'if statement' checks if user entered the correct pin.
                print('Correct pin')
                time.sleep(1)
                break
            else:
                print('Incorrect Pin')
                print('wait 2 minutes to try again')
                time.sleep(120)
                # user has to wait for 2 minutes to try again,
                # the loop goes on and on until user gets the pin correct

yes = 0
# creates a variable and sets the value at '0'
valid_option = True
while valid_option:
    # creates another loop.
    time.sleep(0.75)
    menu = input('''
Please select an Option:


Welcome to National Bank ATM System.
1 - Display Balance
2 - Withdraw Funds
3 - Deposit Funds
4 - Print List  of transactions
9 - Return the Card
    
----> :''')
    # prints the menu as a question, so we don't have to create another variable as a question
    # also I used  3 commas (''' e.g''') because you can  go across lines and still works.
    print()
    if menu == "1":  # this activates if the user enters option 1
        print('Display Balance')  # this says what the user has selected
        print('KES', user_balance)  # then the variable that holds the user balance is displayed.
        time.sleep(0.25)
    elif menu == '2':
        print('Withdraw Funds')
        time.sleep(0.75)
        withdraw_funds = int(input('''
How much would you like to withdraw?
Your options are:
10000:
20000:
50000:
100000:
7 - Other Amount (Must be a multiple of 10):
8 - Return to Main Menu:
9 - Return the Card:

---> : '''))  # this is another menu/question for withdraw_funds
        if withdraw_funds == user_balance:
            print('Congratulations! You have emptied your account. New Account balance : KES 0')
            user_balance = 0
            never = "Withdrew", withdraw_funds
            time.sleep(0.75)

        elif withdraw_funds > user_balance:
            print("You don't have that much money")
            never = 0
            yes = yes - 1
            time.sleep(0.75)

        elif withdraw_funds == 10000:
            print("Successfully withdrawn KES 10000 remaining balance is now", user_balance - 10000)
            user_balance = user_balance - withdraw_funds
            never = "Withdrew", withdraw_funds
            time.sleep(0.75)

        elif withdraw_funds == 20000:
            print("Successfully withdrawn KES 20000 remaining balance is now", user_balance - 20000)
            user_balance = user_balance - withdraw_funds
            never = "Withdrew", withdraw_funds
            time.sleep(0.75)

        elif withdraw_funds == 50000:
            print("Successfully withdrawn KES 50000 remaining balance is now", user_balance - 50000)
            user_balance = user_balance - withdraw_funds
            never = "Withdrew", withdraw_funds
            time.sleep(0.75)

        elif withdraw_funds == 100000:
            print("Successfully withdrawn KES 100000 remaining balance is now", user_balance - 100000)
            user_balance = user_balance - withdraw_funds
            never = "Withdrew", withdraw_funds
            time.sleep(0.75)

        elif withdraw_funds == 7:
            print('Other Amount')
            other_amount = int(input("How much would you like to withdraw? : "))
            if other_amount == user_balance:
                print("Congratulations! You have emptied your account. New Account balance : KES 0")
                user_balance = 0
                never = 'Withdrew', other_amount
                time.sleep(0.75)

            elif other_amount > user_balance:
                print("You don't have that much money")
                never = 0
                yes = yes - 1
                time.sleep(0.75)

            elif other_amount % 10 == 0:
                print("Successfully withdrawn KES", other_amount, "You now have KES", user_balance - other_amount)
                user_balance = user_balance - other_amount
                never = 'Withdrew', other_amount
                time.sleep(0.75)

            else:
                print("Invalid")
                print("Make sure amount is a multiple of 10")
                never = never
                yes = yes - 1
                time.sleep(0.75)

        elif withdraw_funds == 8:
            print()
            never = never
            yes = yes - 1
            time.sleep(0.75)

        elif withdraw_funds == 9:
            print("Thank you for using National Banking ATM System")
            sys.exit()

        else:
            print("Invalid")
            yes = yes - 1

        yes = yes + 1

        if yes > 10:

            trans1 = trans2
            trans2 = trans3
            trans3 = trans4
            trans4 = trans5
            trans5 = trans6
            trans6 = trans7
            trans7 = trans8
            trans8 = trans9
            trans9 = trans10
            trans10 = never

        elif yes == 1:
            trans1 = never

        elif yes == 2:
            trans2 = never

        elif yes == 3:
            trans3 = never

        elif yes == 4:
            trans4 = never

        elif yes == 5:
            trans5 = never

        elif yes == 6:
            trans6 = never

        elif yes == 7:
            trans7 = never

        elif yes == 8:
            trans8 = never

        elif yes == 9:
            trans9 = never

        elif yes == 10:
            trans10 = never

    elif menu == '3':
        print('Deposit Funds')
        add_funds = int(input('''
 Choose an option:
 1 - Deposit
 2 - Return to main menu
 9 - Return Card
 
 ----> : '''))
        if add_funds == 1:
            deposit_funds = int(input("How much would you like to deposit?: "))
            if deposit_funds > 0:
                print("Successfully deposited", deposit_funds, "You now have KES", user_balance + deposit_funds)
                user_balance = user_balance + deposit_funds
                never = 'Deposited', deposit_funds

            elif deposit_funds < 0:
                print("You can't use negative numbers")
                never = never
                yes = yes - 1

        elif add_funds == 2:
            print()
            never = never
            yes = yes - 1

        elif add_funds == 9:
            print("Thank you for using National Banking ATM System: ")
            sys.exit()
            # sys.exit means system command exit code
            # the next 44 lines are the same as before because we just copied them over.
        else:
            print('Invalid, Please select valid option')
            yes = yes - 1

        yes = yes + 1

        if yes > 10:

            trans1 = trans2
            trans2 = trans3
            trans3 = trans4
            trans4 = trans5
            trans5 = trans6
            trans6 = trans7
            trans7 = trans8
            trans8 = trans9
            trans9 = trans10
            trans10 = never

        elif yes == 1:
            trans1 = never

        elif yes == 2:
            trans2 = never

        elif yes == 3:
            trans3 = never

        elif yes == 4:
            trans4 = never

        elif yes == 5:
            trans5 = never

        elif yes == 6:
            trans6 = never

        elif yes == 7:
            trans7 = never

        elif yes == 8:
            trans8 = never

        elif yes == 9:
            trans9 = never

        elif yes == 10:
            trans10 = never

    elif menu == '4':
        print("Print list of transactions")
        time.sleep(0.75)
        print()
        print(trans1)
        print(trans2)
        print(trans3)
        print(trans4)
        print(trans5)
        print(trans6)
        print(trans7)
        print(trans8)
        print(trans9)
        print(trans10)

    elif menu == '9':
        print("Thank you for using National Banking ATM System:")
        sys.exit()

    else:
        print("Please choose a valid option")
