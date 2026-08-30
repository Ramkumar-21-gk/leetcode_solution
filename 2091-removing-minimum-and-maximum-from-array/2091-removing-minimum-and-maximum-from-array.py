class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        return min(
            max(min_index, max_index) + 1,
            n - min(min_index, max_index),
            min_index + 1 + n - max_index,
            max_index + 1 + n - min_index
        )