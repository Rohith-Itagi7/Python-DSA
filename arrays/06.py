# Calculate Sum and Product of Array Elements


arr = [10, 25, 7, 42, 18, 30]

sum = 0
total = 1

for i in range(len(arr)):
    sum += arr[i]
    total = total * arr[i]

print(sum)
print(total)
