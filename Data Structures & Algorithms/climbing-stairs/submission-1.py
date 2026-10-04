class Solution:
    def climbStairs(self, n: int) -> int:
        # Resolving base cases
        if n == 1 or n == 2:
            return n

        # Will be useful for later
        prev = 1
        cur = 2

        # Calculate results from the third
        # stair and beyond
        for stair in range(3, n + 1):
            # Calculate the new result
            total = cur + prev

            # Update the information we require
            prev = cur
            cur = total

        # Return the total amount of ways
        return total