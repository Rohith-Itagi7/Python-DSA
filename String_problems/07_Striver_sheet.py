# Rotate String

class Solution:    
    def rotateString(self, s, goal):
        #your code goes here
        if len(s)!=len(goal):
            return False
        return goal in s+s



# 1. Which pattern does it belong to? 🧠

# Pattern: String Rotation / Circular String

# This is a string manipulation + substring search problem.

# 2. Core Pattern 🧠

# A rotation keeps the same circular order. Duplicate the string (s + s), then check whether goal appears inside it.

# Example:

# s = abcde

# s + s = abcdeabcde

# Possible rotations are hiding inside:

# abcde
# bcdea
# cdeab
# deabc
# eabcd

# So instead of manually performing every shift:

# return goal in s + s
# 3. Keywords to recognize this pattern 🔍

# When you see:

# rotate a string
# shift left/right
# cyclic shift
# circular shift
# move first character to the end
# move last character to the beginning
# can s become goal after shifts?
# is goal a rotation of s?

# 👉 Think:

# s + s + substring check

# 4. Mental Model 🧠

# Don't think:

# "Let me perform shift 1, shift 2, shift 3..."

# Instead think:

# "The characters form a circle. Every rotation is just a different place where I start reading."

# For:

# abcde

# Think:

# a → b → c → d → e
# ↑               ↓
# └───────────────┘

# Starting at a:

# abcde

# Starting at b:

# bcdea

# Starting at c:

# cdeab

# Starting at d:

# deabc

# Starting at e:

# eabcd

# abcdeabcde contains all these possibilities.

# 5. ⭐ Special Line of Code

# The important line is:

# return goal in s + s

# Understand each part:

# s + s
# abcde + abcde
#       ↓
# abcdeabcde
# goal in ...

# in asks:

# "Does this string exist inside that string?"

# Example:

# "cdeab" in "abcdeabcde"

# → True

# Therefore:

# return goal in s + s

# is equivalent to:

# if goal in s + s:
#     return True
# else:
#     return False
# 6. One important safety check ⚠️

# Usually write:

# if len(s) != len(goal):
#     return False

# return goal in s + s

# Why?

# Consider:

# s = "abc"
# goal = "ab"

# "ab" is technically inside "abcabc":

# "ab" in "abcabc"

# → True

# But "ab" cannot be a rotation of "abc" because the lengths differ.

# So:

# if len(s) != len(goal):
#     return False

# handles that case.

# 🧠 Remember This Pattern

# Write this in your notebook:

# Rotation → same length + duplicate the string + check whether goal is a substring.
