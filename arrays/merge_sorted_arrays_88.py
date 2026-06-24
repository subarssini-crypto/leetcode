# Intuition
# Merge two sorted arrays into nums1 in sorted order.

# Approach
# Start from the end of both arrays.
# Compare the largest remaining elements of nums1 and nums2.
# Place the larger element at the end of nums1.
# Continue until all elements of nums2 are merged.

# Complexity
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1