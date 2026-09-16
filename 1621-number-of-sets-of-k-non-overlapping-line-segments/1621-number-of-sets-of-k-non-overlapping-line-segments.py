class Solution:
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7

        # f[i][j] = ways using first i points,
        #           with j segments, and NOT currently drawing
        #
        # g[i][j] = ways using first i points,
        #           with j segments, and currently drawing a segment

        f = [[0] * (k + 1) for _ in range(n + 1)]
        g = [[0] * (k + 1) for _ in range(n + 1)]

        f[1][0] = 1

        for i in range(2, n + 1):
            for j in range(k + 1):

                # We are not drawing at point i
                f[i][j] = (f[i - 1][j] + g[i - 1][j]) % MOD

                # We are drawing a segment
                g[i][j] = g[i - 1][j]

                if j > 0:
                    # Start a new segment
                    g[i][j] += f[i - 1][j - 1]
                    g[i][j] %= MOD

                    # Continue an existing segment
                    g[i][j] += g[i - 1][j - 1]
                    g[i][j] %= MOD

        return (f[n][k] + g[n][k]) % MOD