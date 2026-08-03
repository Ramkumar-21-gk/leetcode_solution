class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        memo = {}

        def solve(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            best = float("-inf")
            total = 0

            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                best = max(best, total - solve(j + 1))

            memo[i] = best
            return best

        diff = solve(0)

        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"