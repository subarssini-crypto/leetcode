# Intuition
# Reverse only the vowels in the string while keeping all other characters in their original positions.

# Approach
# Convert the string into a list of characters.
# Use two pointers, one from the beginning and one from the end.
# If both characters are vowels, swap them.
# Otherwise, move the pointers accordingly until they meet.
# Convert the list back into a string and return it.

# Complexity
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        i=0
        j=len(s)-1
        x="aeiouAEIOU"
        t=""
        while i<j:
            if l[i] in x and l[j] in x:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            elif l[i] not in x and l[j] not in x:
                i+=1
                j-=1
            elif l[i] not in x:
                i+=1
            else:
                j-=1
        for i in l:
            t+=i
        return t