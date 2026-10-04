class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solution: O(n) complexity and O(1) space

        # Extract base information
        cur = cost[1]
        prev = cost[0]

        # Go from the third stair and beyond
        for i in range(2, len(cost)):
            # Store the minimum way to get to the ith step
            total = min(prev, cur) + cost[i]

            # Update our information
            prev = cur
            cur = total

        # Once we are at the top, return either
        # the better choice of taking one or two steps
        return min(cur, prev)