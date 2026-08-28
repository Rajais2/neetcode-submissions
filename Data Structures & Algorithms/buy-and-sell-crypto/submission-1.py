class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Tracking minimums and maximums
        min_cost, max_profit = float('inf'), 0

        # Traversing through all of our prices
        for price in prices:
            # Checking if we have a cheaper cost
            if price < min_cost:
                min_cost = price

            # If we have a bigger profit, update our maximum
            if price - min_cost > max_profit:
                max_profit = price - min_cost

        # Returning the maximum profit we can achieve
        return max_profit

