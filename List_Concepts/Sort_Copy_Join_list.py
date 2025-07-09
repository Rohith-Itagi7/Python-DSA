thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]#sort method is case-sensitive frist it recognise capital letters
thislist.sort()
print(thislist)

#reverse order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)