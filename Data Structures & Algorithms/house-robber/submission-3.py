class Solution:
    def rob(self, nums: List[int]) -> int:
        # Resolving base cases
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Set up to store information
        prev = nums[0]
        cur = max(nums[0], nums[1])

        # Go from the third house and beyond
        for i in range(2, len(nums)):
            # Find the max for that position
            total = max(cur, prev + nums[i])

            # Update our information
            prev = cur
            cur = total

        # Return the max money we can rob
        return cur
