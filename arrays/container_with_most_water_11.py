# Intuition
# Find the maximum amount of water that can be contained between two lines.

# Approach
# Use two pointers, one at the beginning and one at the end.
# Calculate the area formed by the two lines.
# Update the maximum area found so far.
# Move the pointer with the smaller height inward.
# Continue until the pointers meet.

# Complexity
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = 0

        while i < j:
            area = min(height[i], height[j]) * (j - i)
            ans = max(ans, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return ans