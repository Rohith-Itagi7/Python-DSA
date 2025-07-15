x=50
y=60
if x<y:
    print("x is less than y")

# if-else
x=70
y=30
if x>y:
    print("x is greater than y")
else:
    print("X is less than Y")

#elif ladder
age=int(input("Enter your age:"))

if age>18:
    print("You'r dult now")
elif age==18:
    print("Still your a teen age")
elif age==16:
    print("You'r minor")
else:
    print("Still you are child")

# if shorthand
x=30
y=20
if (x>y):print("x is greater than y")

#if-else shorthand
x=50
y=40
print('x >y' if x<y else('x<y'))

a = 2
b = 330
print("A") if a > b else print("B")

# we can also have multiple else statements on the same line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Using Logical Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested if
age=20

if age<20:
   print("Under weight")
   if age==18:
      print("Average Weight")
   else:
      print("Perfect weight")

