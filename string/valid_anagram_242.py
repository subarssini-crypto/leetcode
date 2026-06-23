# Intuition
# Check whether two strings are anagrams of each other.

# Approach
# Convert both strings into lists of characters.
# Sort both lists.
# Compare the sorted lists.
# If they are equal, return True; otherwise, return False.

# Complexity
# Time complexity: O(n log n + m log m)
# Space complexity: O(n + m)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        l1.sort()
        l2.sort()
        return l1==l2