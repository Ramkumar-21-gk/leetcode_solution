class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum=0
        high,low,res=0,0,float('inf')
        n=len(nums)
        while high<n:
            sum=sum+nums[high]
            while sum>=target:
                length=high-low+1
                res=min(res,length)
                sum=sum-nums[low]
                low+=1
            high+=1
        return 0 if res == float('inf') else res

        