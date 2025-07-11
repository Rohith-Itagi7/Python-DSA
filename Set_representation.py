# Set is a collection  of items which is unorderd,unchangeable,No dupliates allowed
set1={"India","Usa","Canada","poland"}
print(type(set1))

#sets with different data types
set1={"India","Usa","Canada","poland"}
set2={1,2,3,4,5,6,7,8,9}
set3={True,False,True,False}

print(set1)
print(set2)
print(set3)

#Different data types in one set
set1={"India",2,True,"Poland",False}
print(set1)

#To check number of items in a set using len() function
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Converting to a set using set() function
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

#Accesing set items using membership operator
set1={"India","Usa","Canada","poland"}
print("India" in set1)

set1={"India","Usa","Canada","poland"}
print("Paris" not in set1)

#Adding a new item and main piont we cant change the items but only we can add thats it
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

#Update() function
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)

print(thisset)



