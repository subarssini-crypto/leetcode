# Intuition
# Find the third distinct maximum number in the array.
# If there are fewer than three distinct numbers, return the maximum number.

# Approach
# Convert the array into a set to remove duplicates.
# Find and remove the largest element, then the second largest.
# If a third distinct maximum exists, return it.
# Otherwise, return the largest element.

# Complexity
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        max1 = max(nums)
        nums.remove(max1)

        if len(nums) != 0:
            max2 = max(nums)
            nums.remove(max2)

        if len(nums) != 0:
            max3 = max(nums)
            return max3
        else:
            return max1