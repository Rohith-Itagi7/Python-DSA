thislist = ["apple", "banana", "cherry"]#looping through list
for i in thislist:
    print(i,end=' ')

thislist = ["apple", "banana", "cherry"]#looping through list using len() function
for i in range(len(thislist)):
    print(i)
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]#looping through while loop
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

# List Comprehension
# newlist = [expression for item in iterable if condition == True] #Syntax
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list=[x for x in fruits if 'a' in x]
print(new_list)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list1=[x for x in fruits if x!='apple']
print(new_list1)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=["hello" for x in fruits]
print(newlist)

newlist = [x for x in range(10) if x<5]
print(newlist)

#It uppercase every item in the list 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list=[x.upper() for x in fruits]
print(new_list)

newlist = [x if x != "banana" else "orange" for x in fruits]
