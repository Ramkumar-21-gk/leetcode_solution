class Solution(object):
    def maxSubarrayLength(self,nums, k):
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):

            # Add nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Window became invalid
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Current window is valid
            ans = max(ans, right - left + 1)

        return ans