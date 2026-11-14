
class Solution(object):
    def threeSum(self, nums):
        result=[]
        n=len(nums)
        nums.sort()

        for num in range(n-2):
            if num>0 and nums[num-1]==nums[num]:
                continue

            target=-1*nums[num]
            left=num+1
            right=n-1

            while left<right:
                sums=nums[left]+nums[right]

                if sums==target:
                    result.append([nums[num],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left-1]==nums[left]:
                        left+=1

                    while left<right and nums[right+1]==nums[right]:
                        right-=1

                elif sums>target:
                    right-=1
                else:
                    left+=1

        return result
