# Count Occurrences of a Target Number in an Array

arr = [5, 2, 7, 5, 9, 5, 3, 2, 8]
target = 5
count=0
for num in arr:
    if target==num:
       count+=1

print(count)
