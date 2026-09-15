class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)

        dp = [0] * (n + 1)

        palindrome = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                
                if s[i] == s[j] and (j - i <= 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for start in range(i - k + 1):
                if palindrome[start][i - 1] and i - start >= k:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]