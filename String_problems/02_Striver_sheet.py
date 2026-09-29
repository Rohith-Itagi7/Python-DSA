# Largest Odd Number in a String

class Solution:  
    def largeOddNum(self, s: str) -> str:
        #your code goes here
        right=len(s)-1

        while right>=0 and int(s[right])%2==0:
            right-=1
        
        if right<0:
            return ""

        left=0

        while left<=right and s[left]=="0":
            left+=1
        
        return s[left:right+1]
