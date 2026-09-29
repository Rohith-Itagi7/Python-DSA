# Isomorphic Strings

class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        #your code goes here
        if len(s)!=len(t):
            return False
        freq={}
        used=set()
        for a,b in zip(s,t):
            if a in freq:
                if freq[a]!=b:
                    return False
            else:
                if b in used:
                    return False
                freq[a]=b
                used.add(b)
        return True

# Isomorphic Strings — Pattern Notes
# 1. Which pattern does it belong to? 🧠
# Hashing / Dictionary + Set

# It is not:

# ❌ Two pointers
# ❌ Sliding window
# ❌ Nested loops
# ❌ Sorting

# The main idea is mapping relationships between two strings.
# Dictionary → "Who maps to whom?"
# Set        → "Is this target already taken?"

# . 🧠 Core Pattern

# Map each source character to one fixed target character, and make sure no two source characters use the same target.
# Every time you see the same source:

# a → ?

# it must give the same answer:

# a → b
# a → b       ✅

# Not:

# a → b
# a → c       ❌

# And every target can belong to only one source:

# a → b
# c → b       ❌


  
