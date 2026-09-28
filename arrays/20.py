# Reverse an array

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left=0
        right=len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1

# How do I recognize this pattern?

# Look for clues like:

# Reverse an array
# Reverse in-place
# No extra array
# Swap elements
# First ↔ last
# Second ↔ second-last
# Operations involving both ends of an array

# When you see "in-place reverse", immediately think:

# 🧠 Two pointers from opposite ends.

# 1. What is the core pattern? 🧠

# Put one pointer at each end → process both elements → move both pointers toward the center → stop when they meet.

# For reversal specifically:

# Swap left and right → move left forward → move right backward.
