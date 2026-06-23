# Intuition
# Find and return the first palindrome string in the array.

# Approach
# Traverse each word in the array.
# Check whether the word is equal to its reverse.
# Return the first palindrome found.
# If no palindrome exists, return an empty string.

# Complexity
# Time complexity: O(n * m)
# Space complexity: O(m)

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f=0
        for i in words:
            if i==i[::-1]:
                return i
                f=1
                break
        if f==0:
            return ""