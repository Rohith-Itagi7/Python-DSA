# Problem statement
# Take the length(L) and breadth(B) of the rectangle as input and find its area.
# Length and breadth must be an integer value and the area will always be in the range of integers.
length, breadth = map(int, input().split())

area = length * breadth

print(area)