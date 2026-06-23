# Intuition
# Sort the array containing 0s, 1s, and 2s in ascending order.

# Approach
# Compare each element with the remaining elements.
# If a smaller element is found, swap them.
# Continue until the entire array is sorted.

# Complexity
# Time complexity: O(n²)
# Space complexity: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]