class Solution:
    def rob(self, nums: List[int]) -> int:
        # Resolving base cases
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Set our dynamic table
        dp = [0] * len(nums)

        # Setting the information we know
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Check from the third house and beyond
        for i in range(2, len(nums)):
            # Update our dynamic table
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # Return the maximum amount of money
        # we can rob
        return max(dp[len(nums) - 1], dp[len(nums) - 2])