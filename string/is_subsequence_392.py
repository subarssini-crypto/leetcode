# Intuition
# Check whether string s is a subsequence of string t.

# Approach
# Use two pointers to traverse both strings.
# If characters match, move the pointer of s.
# Always move the pointer of t.
# If all characters of s are matched, return True; otherwise, return False.

# Complexity
# Time complexity: O(n + m)
# Space complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)