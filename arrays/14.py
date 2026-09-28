# Find the Second Maximum Element; if None, Print -1


large = float("-inf")
second = float("-inf")

for num in arr:
    if num > large:
        second = large
        large = num
    elif num > second and num != large:
        second = num

if second == float("-inf"):
    print(-1)
else:
    print(second)
