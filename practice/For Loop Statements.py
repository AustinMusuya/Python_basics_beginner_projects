# For Loop Statements

for item in {"Python", "Java", "MySQL", "JavaScript"}:
    print(item)

# You can mix data types too
for item1 in ["Python", 2, 5.5, True, False]:
    print(item1)

# You can create multiplication table as well

num = 2
for x in range(1, 11):
    print(num, 'X', x, '=', num * x)

# you can also create an input too
num = float(input("Enter your Number : "))
for x in range(1, 11):
    print(num, 'X', x, '=', num * x)

# Loop through a String

company = ["O", "C", "E", "A", "N"]
for i in company:
    print(i)

# How to use break statement in for loops

company = ['O', 'C', 'E', 'A', 'N']
for i in company:
    if i == 'A':
        break
    print(i)
# note the indentation after the break.
# print command should start on a different indentation

# Continue Statement

company = ["O", "C", "E", "A", "N"]
for i in company:
    if i == 'A':
        print("I got it right!")
        continue
    print(i)

# output says it all.
# example 2

EP_winelist = 'Jameson', 'Gordons', 'Glenfiddich', 'Tanquerray'
for i in EP_winelist:
    if i == 'Glenfiddich':
        print('KingFisher')
        input('Enter preferred drink:')
        continue
    print(i)
# You can play with the code and write your own input as well

# Range

for item in range(5, 200, 5):
    print(item)

'''
The above range is from 5 to 199,once 5 was added,
then it meant that the items within the range 
would be presented as intervals of five in the output as below.
'''

# Nested Loop
'''
Simply put, its a loop constructed within a loop
'''
# Example

for x in range(5):
    for y in range(5):
        print(f'{x},{y}')

# 2D nested loops
# 3 X 3 matrices

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for i in row:
        print(i)
# note the commas when creating matrices.
# the code will not run if there are no commas in between the individual rows.
