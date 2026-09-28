 # Check if the Array is Sorted I

class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
               return False
        return True

        
# Remember this pattern 🧠
# Find ONE bad condition → return False immediately

# Finish the entire loop without finding a bad condition → return True
