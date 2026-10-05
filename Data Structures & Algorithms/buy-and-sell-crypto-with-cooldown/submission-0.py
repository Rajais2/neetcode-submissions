class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Creating our required dynamic tables
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        rest = [0] * len(prices)

        # Setting our base cases
        buy[0] = -prices[0]
        sell[0] = 0
        rest[0] = 0

        # Go from the second day and beyond
        for i in range(1, len(prices)):
            # Updating our tables depending on
            # our choice
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = buy[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sell[i - 1])

        # We want the maximum profit without holding a coin
        return max(sell[-1], rest[-1])