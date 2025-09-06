#It clears the whole list 
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

#It helps to count the repeated digits 
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

#Index is used for accessing items index 
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

fruits = ['apple', 'banana','jackfruit','cherry','bannana']#Finding the postion of 'cherry', but start the search at position 3
x = fruits.index("cherry",3)
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#It reverse the full list 
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
