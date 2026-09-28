# Count Unique and Duplicate Elements in an Array

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

for value, count in freq.items():
    if count == 1:
        uniqueCount += 1
    else:
        duplicateCount += 1
