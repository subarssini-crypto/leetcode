class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for i in d:
            if d[i]>n/2 and d[i]==max(d.values()):
                return i