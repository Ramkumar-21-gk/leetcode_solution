class Solution(object):
    def removeDuplicates(self, nums):
        count=1
        move=1
        cm=0
        n=len(nums)
        while move<n:
            if nums[move]==nums[cm]:
                move+=1
            else:
                cm+=1
                nums[count],nums[move]=nums[move],nums[count]
                count+=1
                move+=1
        return count

        