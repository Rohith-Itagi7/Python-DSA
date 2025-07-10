#using lambda funtion where every itreable the x recieves the current x value 
lis=[lambda x=i: x*10 for i in range(1,6)]

for fun in lis:
    print(fun())

#example-2
square = lambda x: x * x
print(square(5)) 

#example-3
bro= lambda x,y:x+y
print(bro(2,3))

#example-4
num=[1,2,3,4,5]
my_bro=list(map(lambda x:x*x,num))
print(my_bro)

#If-else-lambda 
bear=lambda x,y: x if x>y else y
print(bear(2,3))

#Inside of def function
def make_incrementer(n):
    return lambda x: x + n

inc5 = make_incrementer(5)
print(inc5(10))  # Output: 15

#using filter() with lambda
lis=[3,4,7,9,2,13,6]
lis=filter(lambda x:x%2==1,lis)

for i in lis:
 print(i)

# Apply lambda function to filter values greater than 10 from a list.

liss=[3,4,7,19,2,13,6]

filtered=list(filter(lambda x:(x>10),liss))
for i in filtered:
   print(i)