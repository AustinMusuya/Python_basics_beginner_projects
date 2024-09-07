'#Sequences'
#Lists'

names = ["Harry", "Tom", "Dick", "Austin"]
print(type(names))
print(len(names))
print(names[0:1])
print(names[0:4])
print(names[::-1])
print(names[2:])
print(names[2])
print(names[0])

#append & insert functions
names = ["Harry", "Tom", "Dick", "Austin"]
names.append("monkey")
print(names)

names.insert(5, "Lovely")
print(names)

#removing items in list

names = ["Harry", "Tom", "Dick", "Austin"]
names.remove("Tom")
print(names)
names = ["Harry", "Tom", "Dick", "Austin"]
names.remove("Dick")
print(names)

#sorting items in list in alphabetical order
names = ["Harry", "Tom", "Dick", "Austin"]
names.sort()
print(names)

names.sort(reverse= True)
print(names)

#Joining Lists in 3 ways

names = ["Harry", "Tom", "Dick", "Austin"]
countries = ["France", "Germany", "Kenya", "Turkey"]
#method 1 ( Creating a third variable)

result = names + countries
print(result)

#method 2 (Using 'for' 'i' 'in' 'append/insert function)
names = ["Harry", "Tom", "Dick", "Austin"]
countries = ["France", "Germany", "Kenya", "Turkey"]

for i in countries :
    names.append(i)
print(names)

#method 3 Using extend function
names = ["Harry", "Tom", "Dick", "Austin"]
countries = ["France", "Germany", "Kenya", "Turkey"]
names.extend(countries)
print(names)

letter = ''' we cannot rewrite the same code using append or insert
 as it will literally add the variable suggested including the 
 parantheses.
'''
print(letter)
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