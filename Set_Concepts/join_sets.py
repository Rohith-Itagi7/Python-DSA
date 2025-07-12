set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1|set2|set3|set4
print(myset)

# Join a Set and a Tuple
set1 = {"a", "b", "c"}
set2=(1,2,3)
x=set1.union(set2)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"a", "b", "c"}
set2={1,2,3,"c"}
x=set1.intersection(set2)
print(x)

#Instead of unsing intersection() this can be done using &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# The values True and 1 are considered the same value. The same goes for False and 0
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)