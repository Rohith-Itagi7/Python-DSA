# Half Pyramid Of Stars
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
# Inverted Pyramid Involving Numbers
for i in range(5,0,-1):#here 5 is start & 0 is stop & -1  decrease i by 1, stopping before i reaches 0.
    for j in range(0,i):
        print(i,end="")
    print()

# Full Pyramid
rows=int(input("Enter the number of rows:"))
k=0
for i in range(1,rows+1):
    for j in range(1,(rows-1)+1):
        print("*",end=" ")
        
        while k!=(2*-1):
            print("* ", end="")
            k += 1
    k=0
    print()

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Print spaces
    for space in range(rows - i):
        print(" ", end="")

    # Print stars
    for star in range(2 * i - 1):
        print("*", end="")

    # Newline after each row
    print()


# Inverted Right-angled Triangle
for i in range(0,5):
    for j in range(5,0,-1): 
        if j>i+1:
           print(end=" ")
        else:
            print("*")
    print()        

#Daimond shape
rows = int(input("Enter number of rows: "))
# Upper part of diamond
k = 0
for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
    k = 0
    print()
# Lower part of diamond
k = 0
for i in range(rows - 1, 0, -1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
    k = 0
    print()

