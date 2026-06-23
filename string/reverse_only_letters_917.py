# Intuition
# Reverse only the letters in the string while keeping all non-letter characters in their original positions.

# Approach
# Convert the string into a list of characters.
# Use two pointers, one from the beginning and one from the end.
# If both characters are letters, swap them.
# If a character is not a letter, move the corresponding pointer.
# Convert the modified list back into a string and return it.

# Complexity
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        l=list(s)
        x=""
        while i<j:
            if l[i].isalpha() and l[j].isalpha():
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            elif l[i].isalpha() == False and l[j].isalpha()==False:
                i+=1
                j-=1
            elif l[i].isalpha() == False:
                i+=1
            else:
                j-=1
            
        for i in l:
            x+=i
        return x