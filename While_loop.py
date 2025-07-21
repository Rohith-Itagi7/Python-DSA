#increment using while loop
count=0
while count<5:
    count+=1
    print(count)

# Nested while loop
i=0
while i<5:
    j=0
    while j<5:
        print(i,j)
        j+=1
i+=1

#while loop with breal function.here break function exits from code even if the condition is true.
i=0
while i<5:
   i+=1
   if i==3:
       break
   else:
       print(f"{i}")  

#while_loop using continue,here continue skips the current itreation nd move to next itreartion
i=0
while i<5:
   i+=1
   if i==3:
       continue
   else:
       print(f"{i}")  

#pas in while loop ,here pass do nothing when i==3
j=0
while i<5:
   i+=1
   if i==3:
       pass
   else:
       print("i")  
#While loop using else block
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished without a break.")

#While loop with one condition
count = 1

while count <= 5: print(count); count += 1

