list=["Roy","Rohith","shradha","Virat"]
for names in list:
    print(names)

#Loop Through the Index Numbers
this_list=["Roy","Rohith","shradha","Virat"]
for i in range(len(this_list)):
    print(i)

# Using a While Loop
this_list=["Roy","Rohith","shradha","Virat"]
i=0
while i<len(this_list):
    print(this_list[i])
    i+=1

# Looping Using List Comprehension
names=["brocode","Abhi","Jhon","Vicky"]
[print(name) for name in names]

# Looping Through a String
name="CodingBro"
for i in name:
    print(i)

#Iterating Over a Tuple
city=("Harihar","Mysore","Hubli","Davangere")
for cities in city:
    print(cities)

#Iterating Over a Dictionary
dict={
    1:"One",
    2:"Two",
    3:"Three",
}
for key,value in dict.items():
    print(key,value)

#Loogin using range
for var in range(1,6):
    print(var)

for i in range(2):
    print("OUTER loop number: ",i+1)
    for j in range(3):
        print("Inner loop number: ",j+1)
    print("**********************")