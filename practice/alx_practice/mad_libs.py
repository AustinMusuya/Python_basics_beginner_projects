
"""
Create a Python program that generates a Mad Libs story using conditional statements. 

Here’s what your program should achieve:

Prompt the user: Ask the user for different words following specific prompts, such as a noun, verb, adjective, etc.

Store the user’s input: Use input() to capture the user’s words and store them in variables.

Build the story: Construct a story template with placeholders for the user-provided words.

Conditional Touches (Bonus): Use conditional statements (if, else) to add some variation to the story based on the user’s input.

Display the final story:Print the complete Mad Libs story with the user’s inserted words.

"""


print(
    ''' 
Let's Play Story Builder!
    '''
)

# Describe a day

adjective = str(input('Describe a day (sunny or rainy): '))


if adjective == 'sunny':
    day_description = f"This {adjective} day made me buy some icecream!"
elif adjective == 'rainy':
    day_description = f"On this {adjective} day, I had forgotten to carry my umbrella!"
else:
    adjective = 'normal'
    print("Day selected as normal")
    day_description = f"On this {adjective} day I had nothing planned to do later."

# Describe a monkey

adjective1 = str(input('Describe a monkey (playful/funny): '))

if adjective1 == 'playful':
    monkey_description = f"The {adjective1} monkey could stop swinging on the bars!"
elif adjective1 == 'funny':
    monkey_description = f"The {adjective1} monkey, was making funny faces!"
else:
    adjective1 = 'lazy'
    print("Monkey described as lazy")
    monkey_description = f"The {adjective1} monkey was sleeping and inactive."

# Describe a lion 

adjective2 = str(input('Describe a lion (fierce/scary): '))

if adjective2 == 'fierce':
    lion_description = f"The {adjective2} lion kept on roaring!"
elif adjective2 == 'scary':
    lion_description = f"The {adjective2} lion was barring it's teeth!"
else:
    adjective2 = 'lazy'
    print("Lion described as lazy")
    lion_description = f"The {adjective2} lion was sleeping and inactive."


# Describe an experience

adjective3 = str(input('Describe an experience (great/informative): '))

if adjective3 == 'great':
    experience_description = "This was a great experience."
elif adjective3 == 'informative':
    experience_description = "This was an informative experience."
else:
    adjective3 = 'boring'
    print("Experience selected as boring")
    experience_description = f"This was a {adjective3} experience."

print (f"""
On a beautiful {adjective} day, I went to the zoo.
{day_description}
I saw a funny {adjective1}  monkey swinging from the trees.
{monkey_description}
Then, I spotted a majestic {adjective2} lion lounging in the sun.
{lion_description}  
What a wild and {adjective3} experience!
{experience_description}.
       """)