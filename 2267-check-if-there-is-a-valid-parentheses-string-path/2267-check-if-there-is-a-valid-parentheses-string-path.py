class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Total characters in every path must be even
        if (m + n - 1) % 2 == 1:
            return False

        # First character must be '('
        # Last character must be ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        memo = {}

        def dfs(r, c, balance):
            # Update balance
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

            # Invalid path
            if balance < 0:
                return False

            # Destination
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Already calculated
            if (r, c, balance) in memo:
                return memo[(r, c, balance)]

            # Move down
            down = False
            if r + 1 < m:
                down = dfs(r + 1, c, balance)

            # Move right
            right = False
            if c + 1 < n:
                right = dfs(r, c + 1, balance)

            memo[(r, c, balance)] = down or right

            return memo[(r, c, balance)]

        return dfs(0, 0, 0)