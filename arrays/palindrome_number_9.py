# Intuition
# Check whether the given integer reads the same forward and backward.

# Approach
# Reverse the digits of the number using a loop.
# Compare the reversed number with the original number.
# If both are equal, return True; otherwise, return False.

# Complexity
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        rev=0
        while x>0:
            b=x%10
            rev=rev*10+b
            x=x//10
        if a==rev:
            return True
        else:
            return False