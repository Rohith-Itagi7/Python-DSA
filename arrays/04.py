# Create a Duplicate of an Array

arr = [10, 25, 7, 42, 18, 30]
n=len(arr)
ans=n*[_] # frist I did this but it should not be done it is invalid use this  ans = n * [None]
for i in range(n):
      ans[i]=arr[i]
print(ans)
