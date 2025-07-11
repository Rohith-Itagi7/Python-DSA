# Updating tuple using list
name=("Ronalodo","Messi","Virat","Abd")
name2=list(name)
name2[2]="Sachin"
name=tuple(name2)
print(name)

#Adding a elemt into tuple using list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Removeing items using list
name=("Ronalodo","Messi","Virat","Abd")
name2=list(name)
name2.remove("Messi")
name=tuple(name2)
print(name)

#Unpacking tuples
# In Python, we are also allowed to extract the values back into variables. This is called "unpacking"
name=("Ronalodo","Messi","Virat","Abd")
(green,red,blue,Orange)=name

print(green)
print(red)
print(blue)
print(Orange)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Looping through a tuple
name=("Ronalodo","Messi","Virat","Abd")
for x in name:
    print(x)

name=("Ronalodo","Messi","Virat","Abd")
for x in range(len(name)):
    print(name[x])

#Iterating over a tuple using while loop
name=("Ronalodo","Messi","Virat","Abd")
i=0
while i<len(name):
    print(name[i])
    i+=1

#Join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Count method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#index method
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)