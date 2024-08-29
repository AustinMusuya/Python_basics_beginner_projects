# Functions
'''
below is a function that has a block of code within it.
once you're done writing your block of code,
you can call your function by typing the function name you have assigned.

note that all functions use the key word 'def' at the start when creating them
'''


def greet_user():
    print("Hi Guys!")
    print("You are all awesome")


greet_user()


# multiplication

def multiplication(val1, val2):  # val 1 & val2 below are parameters for the function
    res = val1 * val2
    return res  # keyword return has been used as part of the block of code.


# calling the function:
# multiplication(2,7)
# the function doesn't run when you try to call it as stated above. instead try:
total = multiplication(2, 7)
print(total)
# the code runs
# when you create a variable for the function,
# and a print statement to follow.
''''
note that the function can be called many times and doesn't 
necessarilly need to be under the same variable.
'''
soln = multiplication(5, 14)
print(soln)

tot = multiplication(8, 9)
print(tot)
# all these numbers put in when calling the function are called 'arguments'

# Functions with arguments
'''
functions can be created
to have arguments within them like the multiplication function above
here's another example.
'''


def greet_user_again(name):
    print(f"Hi {name}")
    print('Welcome to Mombasa')


greet_user_again('Austin')
# the parameter above is 'name', so when calling the funciton,
# it has to be included.
# the function once again can be called under a different argument as below.
greet_user_again('Ju$uCH')


def greet_user_again(name, age):
    print(f"Hi {name} {age}")
    print('Welcome to Mombasa')


greet_user_again('Austin', 34)


# Above there are two parameters and consequently two arguments have been included
# age & name.
def greet_user_again(name, age):
    print(f"Hi {name} of age {age}")
    print('Welcome to Mombasa')


greet_user_again("Jusuch", 18)

# *args & *kwargs

'''
this are known as non keyword arguments/arbitary arguments and key word arguments respectively.
they have the asterisks at the begining when putting them up as parameters for a function.
they are primarily applied in situations
where we have no idea of the number of arguments the function will need.
example below
'''


def add_the_values(*num):
    sum = 0
    for n in num:
        sum += n
    print('sum:', sum)


add_the_values(2, 5)
add_the_values(14, 15, 16, 196, 196, 1965, )
add_the_values(515, 15, 151, 51687, 6873876, 87684, 3)


# **kwargs

def intro(**data):
    print("Datatypes Args", type(data))
    for key, value in data.items():
        print("{}:{}".format(key, value))


intro(firstname="Austin", secondname="Musuya", age=34)
