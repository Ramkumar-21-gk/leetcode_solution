class Solution(object):
    def removeDuplicates(self, nums):
        k,off=1,1
        cm=0

        while off<len(nums):
            if nums[cm]==nums[off]:
                off+=1
                continue
            cm+=1
            nums[cm]=nums[off]
            off+=1
            k+=1
        return k

        # unique=1
        # officer=1
        # cm=0
        # n=len(nums)
        # while officer<n:
        #     if nums[officer-1]==nums[officer]:
        #         officer+=1
        #         continue
        #     cm+=1
        #     nums[cm]=nums[officer]
        #     unique+=1
        #     officer+=1
        # return unique
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

        