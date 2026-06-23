# Intuition
# Find the elements that are present in both arrays.

# Approach
# Traverse nums1 and check whether each element is present in nums2.
# Store the common elements in a list and remove duplicates using a set.

# Complexity
# Time complexity: O(n*m)
# Space complexity: O(n)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in nums1:
            if i in nums2:
                l.append(i)
        return list(set(l))