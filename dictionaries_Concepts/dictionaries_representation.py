
# Dictionary items are ordered, changeable, and do not allow duplicates.
my_dict={
    "Name": "Rohith",
    "Year": 2005,
    "Birth_Place": "Bangalore",
}

print(my_dictdict)

thisdict={
    1:"Rohith",
    2:"Rakshitha",
    3:"Manu",
    4:"Venki"
}
print(thisdict[1]) #getting values using key 

print(thisdict.keys())  #getting keys()
print(thisdict.values())

thisdict[6]=["Dr bro"] # Add a new item to the original dictionary, and see that the keys list gets updated as well
#To get length of the dictionary items
print(len(thisdict))
print(thisdict)


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
