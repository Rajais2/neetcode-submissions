class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our various sums
        runningSum = maxSum = nums[0]

        # Traverse through each number
        for index in range(1, len(nums)):
            # If the current number by itself is
            # better, then start a new subarray
            if nums[index] > runningSum + nums[index]:
                runningSum = nums[index]
            else:
                # Otherwise, extend the subarray
                # we're currently on
                runningSum += nums[index]

            # Update our max sum if we have found
            # a new one
            maxSum = max(maxSum, runningSum)

        # Return our max sum we found
        return maxSum