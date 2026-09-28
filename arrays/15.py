# Insert an Element at the Xth Position, Shifting Right

arr = [10, 20, 30, 40, 50]

pos = 3
value = 99

for j in range(len(arr) - 1, pos-1, -1):
    arr[j] = arr[j - 1]

arr[pos] = value

print(arr)
