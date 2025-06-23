list0=["Rohith","Four","Three"]
list1=[1,2,3,4,5,6]
list3=[True,False,True,False]
list_ = ["abc", 34, True, 40, "male"]#list contaning the all different types of data.
print(type(list1))

my=list(("Apple","Orange","Rock"))#Construct list using list()
print(my)

#Accesing list items
my_list=["Rohith","Four","Three"]
print(my_list[1])

my_list=["Rohith","Four","Three"]
print(my_list[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[3:6])
print(thislist[2:])
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2]=["blackcurrant", "watermelon"]
print(thislist)

#Adding list elements
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist=["apple", "banana", "cherry"]
thislist.append("Orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Removing the element from the list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()#removes the last element
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #del function is used to delete list item and even we can delete entier list using del
print(thislist)