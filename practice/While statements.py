#While loop statements
#the program runs non stop. But once the last variable (X=x+1) is inititated,
# then the program refers to the variable and stops when x is equal to 7
x = 5
while x <= 7:
    x = x + 1
    print(x)

print("Completed")

#you can substitute the numbers and make a pattern instead
x = 5
while  x<= 10:
    x = x + 1
    print('$' * x)
#You can create a multiplication table as well
num = 7
x = 1
while  x<= 50:
    x = x + 1
    print(num,'X', x, '=', num * x)

#You can create user input as well

num = float(input("Enter your Number: "))
x = 1
while  x<= 50:
    x = x + 1
    print(num,'X', x, '=', num * x)
