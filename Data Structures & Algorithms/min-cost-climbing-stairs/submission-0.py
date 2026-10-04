class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Creating our dynamic table
        dp = [0] * len(cost)

        # Setting the information we
        # already know
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Go from the second cost and beyond
        for i in range(2, len(cost)):
            # Calculate the minimum
            dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i])

        # Return the better choice when
        # we reach the top
        return min(dp[len(cost) - 2], dp[len(cost) - 1])
