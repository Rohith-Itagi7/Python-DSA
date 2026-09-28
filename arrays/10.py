# A Mismatch Does Not End the Pair Search

arr = [4, 2, 7, 1]
target = 8

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print([i, j])
