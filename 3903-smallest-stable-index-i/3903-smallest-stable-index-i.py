class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)

        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])

        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            # instability score
            if prefix_max - suffix[i] <= k:
                return i

        return -1