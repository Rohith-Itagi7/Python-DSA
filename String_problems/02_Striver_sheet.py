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

# right
#   ↓
# Find RIGHTMOST ODD

# left
#   ↓
# Skip LEADING ZEROS

# s[left:right+1]
#   ↓
# Return the answer


# s[left:right + 1]

# Remember why +1:

# Python slicing:
# start included
# end excluded

# right
# right = len(s) - 1

# Tracks:

# Where the answer should END.

# It moves from right → left until it finds an odd digit.

# left
# left = 0

# Tracks:

# Where the answer should START.

# It moves from left → right while the character is 0

# . What is the core pattern? 🧠

# Find the RIGHTMOST odd digit → keep everything up to it → remove leading zeros.

# Why the rightmost odd digit?

# Because an odd number must end in an odd digit. To make the number as large as possible, we want to keep as many digits as possible.

# So:

# ODD → last digit must be odd
# LARGEST → use the rightmost odd ending
# NO LEADING ZERO → move left past starting zeros

# This is a Greedy + Boundary/Two-Pointer Scanning pattern.

# 2. How do I recognize this pattern?

# Look for these clues:

# Keyword 1: "Odd"

# Immediately think:

# Last digit ∈ {1, 3, 5, 7, 9}
# Keyword 2: "Largest"

# Think:

# Can I keep the longest possible valid portion?

# Keyword 3: "Substring"

# Think:

# I need a continuous section of the original string.

# Keyword 4: "No leading zeros"

# Think:

# I may need to move my left boundary forward.

# Keyword 5: "Large integer"

# Think:

# Keep it as a string, don't actually build a huge integer.
