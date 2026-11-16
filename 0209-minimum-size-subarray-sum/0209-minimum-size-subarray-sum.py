class Solution(object):
    def minSubArrayLen(self, target, nums):
        low=0
        window=0
        result=float('inf')

        for high in range(len(nums)):
            window+=nums[high]

            while window>=target:
                result=min(result,high-low+1)
                window-=nums[low]
                low+=1


        return 0 if result==float('inf') else result 
