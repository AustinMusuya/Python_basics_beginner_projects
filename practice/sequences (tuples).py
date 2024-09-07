#Sequences
#Tuples in Python
'''Another Characteristic that differentiate them from list
is that they use '()' parenthesis instead if of the '[]' in Lists '''

#Example

tuple_list = ("Austin", "Harry", "Nick", "Ted" )
print(tuple_list)

''' if you try to append, insert, extend the variable (tuple_list) 
nothing happens. Note, Tuples are immutable  '''

#Updating Tuples
''' to update a tuple list inorder to edit it, you need to create a variable
and typecast the previous variable of the tuple into 'list' first i.e (tuple_list). 
then create another variable to type cast the new variable to a 'tuple'.
'''
tuple_list = ("Austin", "Harry", "Nick", "Ted" )
l = list(tuple_list)
l[0] = "John"
print(l)
t = tuple(l)
print(t)
'''
the newly created variables here are 'l' & 't'
'''
t = tuple_list

#Joining tuples
tuple_list = ("Austin", "Harry", "Nick", "Ted" )
countries = ("France", "Germany", "Kenya", "Turkey")

join_tuple = tuple_list + countries
print(join_tuple)

#tuple lists cannot be appended or inserted
'''
List is a collection which is ordered and changeable. 
Allows duplicate members.
Tuple is a collection which is ordered and unchangeable.
Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed.
No duplicate members.
Dictionary is a collection which is ordered** and changeable.
No duplicate members.
'''