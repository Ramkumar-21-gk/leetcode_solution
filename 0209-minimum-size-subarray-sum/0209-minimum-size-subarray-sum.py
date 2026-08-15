class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        low=0
        high=0
        mysum=0
        min_len = float('inf')
        if n==0:
            return 0
        while (high<n):
            mysum+=nums[high]
            while mysum>=target:
                min_len=min(min_len,high-low+1)
                mysum=mysum-nums[low]
                low+=1
            high+=1
        if min_len == float('inf'):
            return 0
            
        return min_len

        