class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a dynamic table
        dp = [0] * (n + 1)

        # Loop from 1 up to n
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (1 if i % 2 != 0 else 0)

        # Our dynamic table contains
        # the final answer
        return dp