#Dictionaries

customer = { "name": "Austin Musuya",
             "address": "2533 Mombasa, kenya",
             "order": "Mustang model GT"
}
print(customer)
print(type(customer))

'''Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*,
changeable and do not allow duplicates.
'''
customer = {"name": "Austin Musuya",
            "address": "2533 Mombasa, kenya",
            "order": "Mustang model GT"
}
print(customer["name"])
'''Dictionaries can be updated as well
'''

customer["name"] = "Lord Ju$uCH"
customer["phone_number"] = 254724966576
print(customer)

'''Dictionaries can be removed as well
'''
customer = { "name": "Austin Musuya",
             "address": "2533 Mombasa, kenya",
             "order": "Mustang model GT"
}
customer.pop("name")
customer["gender"] = "male"
print(customer)

#Nested dictionaries
'''A dictionary can contain dictionaries,
this is called nested dictionaries.
'''

customer1 = { "name": "Austin Musuya",
             "address": "2533 Mombasa, kenya",
             "order": "Mustang model GT"
}

customer2 = { "name": "John Hart",
             "address": "2533 Mombasa, kenya",
             "order": "Mustang model GT"
}

customer3 = { "name": "Steve Keynan",
             "address": "2533 Mombasa, kenya",
             "order": "Mustang model GT"
}

mynest = {"cust1" : customer1,
          "cust2" : customer2,
          "cust3" : customer3
          }
print(mynest)
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