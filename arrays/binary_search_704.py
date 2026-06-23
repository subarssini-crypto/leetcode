# Intuition
# Find the target element in a sorted array using Binary Search.

# Approach
# Use two pointers, low and high, to represent the search range.
# Find the middle element.
# If the middle element is the target, return its index.
# If the target is greater, search the right half.
# Otherwise, search the left half.
# If the target is not found, return -1.

# Complexity
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1