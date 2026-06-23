# Intuition
# Find the extra character present in string t.

# Approach
# Convert both strings into lists.
# Remove from t every character that is found in s.
# The remaining character in t is the extra character.
# Return that character.

# Complexity
# Time complexity: O(n²)
# Space complexity: O(n)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1=list(s)
        l2=list(t)
        for i in l1:
            if i in l2:
                l2.remove(i)
        for i in l2:
            return i