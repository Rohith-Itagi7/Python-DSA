tuple=("Rohan","Aliya","Karthik araan","Virat","David")
print(tuple)

#Tuples containing different data types
Multiple_data_types=("1", 5 ,True,False)
print(Multiple_data_types)

Dishes=("Benne Dose", "Idle", "Palav", "Vadapav", "Cheese balls","Palav") #Tuple containg duplicate values
print(len(Dishes) #len function is used to  know number of tuple elementd
print(Dishes[1])
print(Dishes[2:])
#Acessing using negative index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Representing a one tuple(,) is main then only it can be tuple
name=("Rohith",)     
print(type(name))

#Not a tuple 
name=("Rohith")     
print(type(name))

# To check wheather the item is present or not
cities=("Dvg","Hrr","Rnr","Bnglr","Rnr")
if "Rnr" in cities:
    print("yes")
else:
    print("No")
