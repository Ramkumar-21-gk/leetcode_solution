class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left=i+1
            right=len(nums)-1
            target=-nums[i]

            while left<right:
                sum=nums[left]+nums[right]
                if sum==target:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left]==nums[left-1]:
                        left+=1
                    while left < right and nums[right]==nums[right+1]:
                        right-=1
                elif sum>target:
                    right-=1
                else:
                    left+=1
        return result
