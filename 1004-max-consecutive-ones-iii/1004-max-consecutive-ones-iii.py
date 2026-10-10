class Solution(object):
    def longestOnes(self, nums, k):
        low,res=0,0
        zeros=0
        for high in range(len(nums)):
            if nums[high]==0:
                zeros+=1
            while zeros>k:
                if nums[low]==0:
                    zeros-=1
                low+=1

            length=high-low+1
            res=max(length,res)
        return res