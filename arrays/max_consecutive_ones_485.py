# Intuition
# Find the maximum number of consecutive 1s in the array.

# Approach
# Traverse the array and count consecutive 1s.
# Reset the count when a 0 is encountered.
# Keep track of the maximum count found.

# Complexity
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        mc=0
        for i in nums:
            if i==1:
                c+=1
                mc=max(mc,c)
            else:
                c=0
        return mc