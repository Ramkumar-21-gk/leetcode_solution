class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        sum=0
        low,high=0,0
        res=float('inf')
        while high<n:
            sum=sum+nums[high]
            while sum>=target:
                leng=high-low+1
                res=min(res,leng)
                sum=sum-nums[low]
                low+=1
            high+=1

        return 0 if res==float('inf') else res     