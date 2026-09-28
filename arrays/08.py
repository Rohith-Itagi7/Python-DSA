# An Array Is Sorted Only When Every Adjacent Pair Agrees


arr = [10, 15, 20, 25, 30, 35]

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        print(arr[i], arr[i + 1])
