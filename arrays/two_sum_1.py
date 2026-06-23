class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        for i in range(len(nums)):
            c=target-nums[i]
            if c in d:
                l.append(d[c])
                l.append(i)
            d[nums[i]]=i
        return l

        