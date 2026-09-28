# Leetcode 125 the answer is different from this
# Reverse a String II

class Solution: 
    def reverseString(self, s):
        #your code goes here
        left=0
        right=len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return s

# Reverse String — Two-Pointer Pattern
# 1. What is the core pattern? 🧠

# Take the leftmost and rightmost elements → swap them → move both pointers inward → repeat until they meet.
# 2. How do I recognize this pattern?

# Look for clues like:

# reverse an array/string
# reverse in-place
# rearrange from both ends
# swap first and last
# swap outer elements
# without using extra array
# reverse the order of elements
# Recognition rule

# If you see:

# "Reverse something in-place"

Your recognition cheat sheet
Problem says...	Think...
Reverse in-place	     Two pointers + swap
Palindrome           	Two pointers + compare
Find an element       	Search + return index
Count elements	        Counter + increment
Maximum	Track          largest so far
Minimum	Track          smallest so far
