# Intuition
# Find the square of each element and return the squares in sorted order.

# Approach
# Traverse the array and store the square of each element in a new list.
# Sort the new list and return it.

# Complexity
# Time complexity: O(n log n)
# Space complexity: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            l.append(i*i)
        l.sort()
        return l