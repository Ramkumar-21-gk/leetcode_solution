class Solution(object):
    def longestSubsequence(self, nums):
        xor = 0

        for num in nums:
            xor ^= num

        if xor != 0:
            return len(nums)

        # XOR of all elements is 0
        for num in nums:
            if num != 0:
                return len(nums) - 1

        return 0