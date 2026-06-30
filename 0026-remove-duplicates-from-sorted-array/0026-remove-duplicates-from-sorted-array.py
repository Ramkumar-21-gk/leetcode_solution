class Solution(object):
    def removeDuplicates(self, nums):
        element=0
        unique_element=1
        move=1
        while move<len(nums):
            if nums[move]==nums[move-1]:
                move+=1
                continue

            element+=1
            nums[element]=nums[move]
            move+=1
            unique_element+=1
        return unique_element

obj=Solution()
obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        