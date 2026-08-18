class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        count = {}

        for i in range(n - k + 1):
            window = nums[i:i + k]
            for x in set(window):
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans