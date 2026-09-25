class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our various sums
        runningSum, maxSum = 0, float('-inf')

        # Traverse through each number
        for num in nums:
            # If the current number by itself is
            # better, then start a new subarray
            if num > runningSum + num:
                runningSum = num
            else:
                # Otherwise, extend the subarray
                # we're currently on
                runningSum += num

            # Update our max sum if we have found
            # a new one
            maxSum = max(maxSum, runningSum)

        # Return our max sum we found
        return maxSum