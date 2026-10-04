class Solution:
    # Creating a helper function
    def linearRob(self, lower, upper, nums) -> int:
        # Initialize our trackers
        prev = 0
        cur = 0

        # Lower and upper are inclusive boundaries
        for i in range(lower, upper + 1):
            # Calculate the max money for that position
            total = max(cur, prev + nums[i])

            # Update trackers
            prev = cur
            cur = total

        # Return the maximum amount of money
        # we can rob
        return max(prev, cur)
    
    def rob(self, nums: List[int]) -> int:
        # Resolving base cases
        if len(nums) <= 1:
            return 0 if len(nums) == 0 else nums[0]

        # Store the number of houses
        n = len(nums)

        # Return the best choice between whether
        # or not to exclude the first house
        return max(self.linearRob(1, n - 1, nums), self.linearRob(0, n - 2, nums))