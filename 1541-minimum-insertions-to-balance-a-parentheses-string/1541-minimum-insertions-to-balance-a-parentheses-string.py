class Solution(object):
    def minInsertions(self, s):
        ans = 0
        right = 0

        for ch in s:
            if ch == '(':
                right += 2

                if right % 2 == 1:
                    ans += 1
                    right -= 1

            else:
                right -= 1

                if right < 0:
                    ans += 1
                    right = 1

        return ans + right