# Intuition
# Find the shortest distance from each character in the string to the given character c.

# Approach
# Store all indices where c occurs.
# For each position in the string, calculate its distance to every occurrence of c.
# Take the minimum distance and store it in the result list.
# Return the result list.

# Complexity
# Time complexity: O(n * k)
# Space complexity: O(n + k)

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        x=[]
        l=[]
        for i in range(len(s)):
            if s[i]==c:
                x.append(i)
        for i in range(len(s)):
            res=[]
            for j in x:
                res.append(abs(i-j))
            l.append(min(res))
        return l