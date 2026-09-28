# Delete an Element at the Xth Position, Shifting Left

arr = [8, 3, 6, 2, 9]
x = 3

delete_index = x - 1

for i in range(delete_index, len(arr) - 1):
    arr[i] = arr[i + 1] #I got confuse here it's shifting only not swapping

del arr[-1] 

print(arr)
