class Solution(object):
    def removeDuplicates(self, nums):
        cm=0
        off=1
        while off<len(nums):
            if nums[off-1]==nums[off]:
                off+=1
                continue
            cm+=1
            nums[cm]=nums[off]
            off+=1
        return cm+1
            