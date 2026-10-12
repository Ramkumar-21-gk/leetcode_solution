
class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        count = [0] * 31

        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    count[i] += 1

        ans = 0

        for _ in range(k):
            x = 0

            for i in range(31):
                if count[i] > 0:
                    x |= (1 << i)
                    count[i] -= 1

            ans = (ans + x * x) % MOD

        return ans

