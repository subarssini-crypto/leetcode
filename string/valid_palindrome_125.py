# Intuition
# Check whether the given string is a palindrome after removing non-alphanumeric characters
# and ignoring letter case.

# Approach
# Traverse the string and keep only alphanumeric characters.
# Convert the cleaned string to lowercase.
# Compare it with its reverse.
# If both are equal, return True; otherwise, return False.

# Complexity
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                x+=i
        if x.lower()==x[::-1].lower():
            return True
        else:
            return False