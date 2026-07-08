class Solution(object):
    def maxProduct(self, nums):
        minend=nums[0]
        maxend=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):
            v1=nums[i]
            v2=minend*nums[i]
            v3=maxend*nums[i]
            maxend=max(v1,max(v2,v3))
            minend=min(v1,min(v2,v3))
            res=max(res,minend,maxend)
        return res

        