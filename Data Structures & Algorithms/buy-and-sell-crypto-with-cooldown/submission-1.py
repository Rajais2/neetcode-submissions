class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Create our 2D dynamic table
        # 0 = buy/holding
        # 1 = sell/cooldown
        # 2 = rest
        dp = [[0] * 3 for _ in range(len(prices))]

        # Set our base cases
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        # Fill the table starting from day 1
        for i in range(1, len(prices)):
            # Holding a stock:
            # Either keep holding, or buy today after resting
            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 1][2] - prices[i]
            )

            # Selling today:
            # We must have been holding yesterday
            dp[i][1] = dp[i - 1][0] + prices[i]

            # Resting:
            # Either keep resting, or cooldown ends
            dp[i][2] = max(
                dp[i - 1][2],
                dp[i - 1][1]
            )

        # We cannot finish while holding a stock
        return max(dp[-1][1], dp[-1][2])