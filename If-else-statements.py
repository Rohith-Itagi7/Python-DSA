#if statement
score_a=60
score_b=40

if score_a> score_b:
    print("You have passed")

#if-else statement
score_a=60
score_b=40

if score_a> score_b:
    print("You have passed")
else:
    print("You have failed")

#elif ladder with comparision operator
score_a=60
score_b=40

if score_a >= score_b:
    print("You have passed")
elif score_a<score_b:
    print("You have too wait for result")
elif score_a <= score_b:
    print("Vist Examination hall")
else:
    print("You have failed")
    
#Short-hand if
a=10
b=20
if (a>b): print('a is  not a greater than b')

#if-else shorthand
a=10
b=20
print('a>b' if a>b else ('a<b'))    

print("A") if a<b else print("B")

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
      if age<=18:
        print("Perfect weight")




