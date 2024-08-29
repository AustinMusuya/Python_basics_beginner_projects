# Data types

# A String Data types
# 1 Double string Data type
first_name = "Austin"
last_name = "_Musuya"
print(first_name + last_name)
print("type of names:", type(first_name + last_name))

# 2 single String data type
a = "Jameson"
b = '_on the rocks'
print(a + b)
print(type(b))
print("type of variables 'a' & 'b':", type(a + b))

# B Numeric Datatypes
# 1 interger Data type
a = 2
b = 67
c = a + b
print(c)
print("type of variable 'c':", type(c))

# 2 Float Data type
price_x = 30.654
price_y = 45.213
print(price_y + price_x)
print(type(price_y))
print("type of prices 'y' and 'x':", type(price_y + price_x))

# 3 Complex Data type
p = 100 + 3j
print(p)
print("type of variable'p':", type(p))

# C Boolean Data type
rainy_day = True
sunny_day = False
print(rainy_day)
print(type(rainy_day))
print(sunny_day)
print(type(sunny_day))

# D Sequence Datatypes
# 1 tuple datatype
a = 1, 2, 3, 4, 5
print(a)
print("type of variable 'a'", type(a))

# 2 List type
list = ["apples", "bananas", "mangoes"]
print(list)
print("type of list", type(list))

# 3 Range type
fruits = range(7)
print(fruits)
print("type of fruits:", type(fruits))

# E set data type
# 1 set type
mylist = {1, 2, 3}
print(mylist)
print(type(mylist))

# 2 frozenset type
mylist_2 = frozenset({"apple", "bananas", "grapes"})
print(mylist_2)
print(type(mylist))

# F mapping Datatype
x = {"name": "John", "age": 36}
print(x)
print(type(x))

# G Binary Datatypes
# 1bytes
german_juice = b"heloo"
print(german_juice)
print(type(german_juice))

# 2 bytearray
german_juice2 = bytearray(5)
print(german_juice2)
print(type(german_juice))

# 3 memoryview
germanjuice_3 = memoryview(bytes(5))
print(germanjuice_3)
print(type(germanjuice_3))
