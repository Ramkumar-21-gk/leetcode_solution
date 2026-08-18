class Solution(object):
    def longestOnes(self, nums, k):
        low,res=0,0
        freq={}
        for high in range(len(nums)):
            freq[nums[high]]=freq.get(nums[high],0)+1
            while freq.get(0, 0) > k:
                freq[nums[low]]-=1
                low+=1
            
            length=high-low+1
            res=max(res,length)
        return res
        