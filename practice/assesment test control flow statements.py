# Assesment

'''
Prepare a python program to find
the factorial of a number provided by the user input.
note:
The factorial number is a product of all the integers from 1 to that given number.
For example the factorial number of 6 is 1*2*3*4*5*6= 720.
Factorial is not defined for negative numbers
and the factorial of zero is one 0! = 1.

Using for loop to implement the factorial of a number program

'''
# if you want to change the input value for a different result.
#num = 6

# to take input from the user
num = int(input('Enter your Number:'))

fact = 1
# check if the number is positive, negative or zero
if num < 0:
    print('Sorry factorial is not defined for negative numbers')

elif num == 0:
    print('Factorial of 0 is 1')

else:
    for i in range(1, num, 1):
        factorial = fact*i

        print(factorial,'is', num,fact)

# code needs revisiting!

