 # Valid Anagram
class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        if len(s) != len(t):
            return False
        frq={}
        for ch in s:
            frq[ch]=frq.get(ch,0)+1
        for ch in t:
            if ch not in frq:
                return False

            frq[ch]-=1

            if frq[ch]<0:
                return False
        return True

#   1. Which pattern does it belong to? 🧠

# Pattern: Hashing → Frequency Counting

# We use a dictionary (dict) to count how many times each character appears.

# 2. What is the core pattern? 🧠

# Anagram = same characters + same frequencies → order does NOT matter.

# Think:

# First string → count characters
# Second string → consume/check those counts
# Anything missing or overused → False
# Everything matches → True

# Example:

# "anagram" → a:3, n:1, g:1, r:1, m:1

# "nagaram" → same frequencies → ✅ Anagram

# 3. Keywords to identify this pattern 🔍

# When the problem says:

# anagram
# rearrangement of characters
# same characters
# same frequency
# same letters
# order doesn't matter
# contains the same characters
# rearranged version
# exactly the same number of each character

# 👉 Think:

# Frequency Dictionary / Counter

# Recognition shortcut

# "Same elements, but order doesn't matter" → Frequency Counting

# 4. What do we track?

# Main thing:

# freq = {}

# It answers:

# "How many times does each character occur?"

# For:

# s = "aabbc"

# we build:

# a → 2
# b → 2
# c → 1
# 5. Edge Cases ⚠️
# ① Different lengths
# s = "abc"
# t = "ab"

# ❌ Not anagram.

# Why?

# Anagrams must contain the same total number of characters.

# ② Same characters but different frequencies
# s = "aab"
# t = "abb"

# ❌ Not anagram.

# Both contain a and b, but:

# s → a:2, b:1
# t → a:1, b:2

# This is why simply checking:

# if ch in t

# is not enough.

# ③ Character completely missing
# s = "abc"
# t = "abd"

# ❌ c is missing from t.

# ④ Duplicate characters
# s = "aabb"
# t = "bbaa"

# ✅ Anagram.

# Order changed, frequencies stayed the same.

# ⑤ Empty strings
# s = ""
# t = ""

# Usually:

# ✅ Anagram

# Both contain zero characters.

# ⑥ Single character
# s = "a"
# t = "a"

# ✅

# s = "a"
# t = "b"

# ❌

# ⑦ Case sensitivity
# s = "Listen"
# t = "silent"

# Whether this is an anagram depends on the problem's rules.

# If case-sensitive:

# L ≠ l

# If the problem says to ignore case, convert both to lowercase first.

# Don't assume normalization unless the problem says so.

# ⑧ Spaces / punctuation

# Example:

# s = "a b"
# t = "ab"

# Whether spaces should count depends on the problem.

# Again:

# Follow the exact problem statement.

# 🧠 Remember This Pattern

# Write this in your DSA notebook:

# Anagram → same characters + same frequencies, order doesn't matter → use frequency counting.

# Ultra-short version:
# Same elements
# + Same frequency
# + Different order allowed
# = Frequency Counting

# And the reusable mental template is:

# Build counts → consume counts → missing/overused → False → finish → True
