# Intuition
# Reverse the given character array in-place.

# Approach
# Use two pointers, one at the beginning and one at the end.
# Swap the characters at both pointers.
# Move the left pointer forward and the right pointer backward.
# Continue until the pointers meet.

# Complexity
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1