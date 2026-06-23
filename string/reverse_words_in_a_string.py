# Intuition
# Reverse the order of words in the given string.

# Approach
# Split the string into words.
# Reverse the list of words.
# Join them back into a string with a single space between words.
# Remove any leading or trailing spaces and return the result.

# Complexity
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l1=l[: :-1]
        x=" ".join(l1)
        return x.strip()