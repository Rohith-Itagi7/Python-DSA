# Tuples are ordered list unchangeable and no duplicates value
thistuple = ("apple", "banana", "cherry")
print(thistuple)

cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")#Tuples containing duplicate value
print(cities)

cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")# how many Tuples using len() function
print(len(cities))

#Representing a one tuple(,) is main then only it can be tuple
name=("Rohith",)     
print(type(name))

#Not a tuple 
name=("Rohith")     
print(type(name))

#Tuple contaning multiple values
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Tuples containing different data types
greeting=(1,False,"Rohith",True)
print(greeting)

cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")
print(cities[1])

cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")
print(cities[2:])

#Accesing using negative index
cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")
print(cities[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# To check wheather the item is present or not
cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")
if "Rnr" in cities:
    print("yes")
else:
    print("No")
