#Sets
'''
sets are characterized by curly parentheses different from tuples '()' & lists '[]'
'''
#adding items in set
nationalities = {"German", "British", "Jamaican", "Kenyan", "Tanzanian",}
print(nationalities)
nationalities.add("American")
print(nationalities)

#removing items in sets
nationalities = {"German", "British", "Jamaican", "Kenyan", "Tanzanian",}

nationalities.remove("German")
print(nationalities)

#joining data sets

nationalities = {"German", "British", "Jamaican", "Kenyan", "Tanzanian",}
states = {"Ohio", "California", "Wyoming", "Nebraska", "Arizona", "Missouri"}

join = nationalities.union(states)
print(join)



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