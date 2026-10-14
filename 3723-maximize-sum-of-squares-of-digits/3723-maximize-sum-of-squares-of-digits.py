class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if num * 9 < sum:
            return ""

        ans = ""

        while num > 0:
            digit = min(9, sum)
            ans += str(digit)
            sum -= digit
            num -= 1

        return ans