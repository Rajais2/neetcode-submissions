class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create our 2D dynamic table
        dp = [[0] * n for _ in range(m)]

        # All cells in the first row have
        # one unique path
        for i in range(n):
            dp[0][i] = 1

        # All cells in the first column have
        # one unique path
        for j in range(m):
            dp[j][0] = 1

        # Fill out the rest of the table
        for i in range(1, m):
            for j in range(1, n):
                # We essentially just add the number
                # of unique paths from either traversing
                # right or down to the current cell
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The final cell has our answer
        return dp[m - 1][n - 1]