# Create Compact Odd and Even Arrays with Independent Write Positions

arr = [10, 25, 7, 42, 18, 30]

odds = []
even = []

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odds.append(num)

print(odds)
print(even)
