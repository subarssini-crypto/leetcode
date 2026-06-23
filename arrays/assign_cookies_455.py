# Intuition
# Assign cookies to children so that the maximum number of children are content.

# Approach
# Sort both arrays.
# Use two pointers to compare the greed factor and cookie size.
# If the cookie can satisfy the child, increase the count and move both pointers.
# Otherwise, move to the next cookie.
# Return the total number of content children.

# Complexity
# Time complexity: O(n log n + m log m)
# Space complexity: O(1)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        k=0
        i=0
        j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                 k+=1
                 i+=1
                 j+=1
            else:
                 j+=1
        return k