# Three Distinct Elements with a Target Sum

arr = [3, 6, 4, 8, 1]
target = 12

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == target:
                print([i, j, k])
