class Solution(object):
    def removeDuplicates(self, nums):
        unique=1
        officer=1
        cm=0
        n=len(nums)
        while officer<n:
            if nums[officer-1]==nums[officer]:
                officer+=1
                continue
            cm+=1
            nums[cm]=nums[officer]
            unique+=1
            officer+=1
        return unique
        # count=1
        # move=1
        # cm=0
        # n=len(nums)
        # while move<n:
        #     if nums[move]==nums[cm]:
        #         move+=1
        #     else:
        #         cm+=1
        #         nums[count],nums[move]=nums[move],nums[count]
        #         count+=1
        #         move+=1
        # return count

        