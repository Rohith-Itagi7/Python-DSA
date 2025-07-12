# Dictionary items are ordered, changeable, and do not allow duplicates.
this_dict={
    "name":"Rohith",
    "Birth":1976,
    "place":"Bangslore"
}
print(this_dict)

#getting keys()
x = this_dict.keys()

#getting values using key 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#To get length of the dictionary items
print(len(thisdict))

# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Using the dict() method to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) 

car["color"] = "white"
print(x)

#Getting values
x = thisdict.values()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

# The items() method will return each item in a dictionary, as tuples in a list
x = thisdict.items()
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"

print(x)

# To determine if a specified key is present in a dictionary use the in keyword
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")