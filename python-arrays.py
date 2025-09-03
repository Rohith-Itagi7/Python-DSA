#Actually arrays are represented in the form of list of an elements ,if you want to perform or to work with array you will have to import a library like numpy
#Arrays have the same methods of list
"""Creating an array """
bikes=["hoda","duke","appache"]

# Access the Elements of an Array
x = bikes[0]

# Modify the value
bikes[0]="Ktm"

# Delete the element
bikes.remove("Volvo")

# Add one more element 
bikes.append("Honda")

# Looping Array Elements
for x in bikes:
  print(x)
