class Solution(object):
    def searchRange(self, nums, target):
        def first():
            low,high=0,len(nums)-1
            ans=-1
            while low<=high:
                guess=(low+high)//2
                if nums[guess]<target:
                    low=guess+1
                elif nums[guess]>target:
                    high=guess-1
                else:
                    ans=guess
                    high=guess-1
            return ans
        def last():
            low,high=0,len(nums)-1
            ans=-1
            while low<=high:
                guess=(low+high)//2
                if nums[guess]<target:
                    low=guess+1
                elif nums[guess]>target:
                    high=guess-1
                else:
                    ans=guess
                    low=guess+1
            return ans

        return [first(),last()]
                

        