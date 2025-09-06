#Clear method
fruits = {"apple", "banana", "cherry"}
fruits.clear()

print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)

print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 

print(z)

#removes an item from a list 
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

#delets the last item in the list 
fruits = {"apple", "banana", "cherry"}
fruits.pop()

print(fruits)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)

print(z)
