# Intuition
# Merge two strings by taking characters alternately from each string.

# Approach
# Traverse up to the length of the longer string.
# Add a character from word1 if available.
# Add a character from word2 if available.
# Return the merged string.

# Complexity
# Time complexity: O(n + m)
# Space complexity: O(n + m)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:  
        s=""    
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                s+=word1[i]
            if i<len(word2):
                s+=word2[i]
        return s