# Write a program that takes three numbers a,b, and c as input and prints the largest number amongst them.
a,b,c=map(int,input().split())

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
