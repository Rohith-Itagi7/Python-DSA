my_list=["Football","Cricket","KHo-Kho","Volleyball"]
print(my_list)

Foods=["1",3,True,] #It holds different data types
print(Foods)

Cities=["Davngere","Harihar","Bangalore","Shivomoga","Madikeri"]
print(Cities[1])
print(Cities[-1])  # last element

Habits=["Walk","Jog","Meditation","Book","Sleeping early"]
Habits[0]="Dance"  #Replacing the Elements
Habits[1:3]=["flourish brain","Helping others"]
print(Habits)

#Accesing the list elements
Cities=["Davngere","Harihar","Bangalore","Shivomoga","Madikeri"]
print(Cities[0:]) 
print(Cities[2:4])
print(Cities[:-1]) #print except last element
print(Cities[::2]) #skipping 2 elements
print(Cities[::-1]) #printing reverse oerder

fav_stars=["Yash","Darshan","Sudeep","yograj"]
fav_stars.append("Rohith")
print(fav_stars)

fav_stars=["Yash","Darshan","Sudeep","yograj"]
fav_stars.remove("Yash")
print(fav_stars)

fav_stars=["Yash","Darshan","Sudeep","yograj"]
fav_stars.insert(3,"Yash")
print(fav_stars)

fav_stars=["Yash","Darshan","Sudeep","yograj"]
fav_stars.extend(["Ranveer"])
print(fav_stars)

fav_stars=["Yash","Darshan","Sudeep","yograj"]
fav_stars.index("Darshan")
print(fav_stars)

fav_stars=["Yash","Darshan","Sudeep","yograj"]
fav_stars.count("Yash")
gav_stars.reverse()
print(fav_stars)

fav_stars=["Yash","Darshan","Sudeep","yograj"]
print(fav_stars.pop()) # delete the last item in list
print(fav_stars.pop("0"))
print(fav_stars.clear()) # It helpsto make a list empty


del fav_stars  # It is used to delete entire list
del fav_stars[0]  


num=[1,6,4,3,5,6]
num.sort()
print(num)

num=[1,6,4,3,5,6]
num.sort( Reverse= True)
print(num)

#Nested Lists
#ists can contain other lists, allowing you to create nested lists. This can be useful for storing matrix-like data structures.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)
