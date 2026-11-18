class Solution(object):
    def longestOnes(self, nums, k):
        freq={}
        left=0
        result=0
        for right in range(len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1
            while freq.get(0,0)>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1

            result=max(result,right-left+1)
        return result
            
        