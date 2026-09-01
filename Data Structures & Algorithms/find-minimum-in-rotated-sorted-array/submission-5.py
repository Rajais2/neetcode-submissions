class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Defining our left and right pointers
        left, right = 0, len(nums) - 1

        # Not <= because we want to stop when left == right
        while left < right:
            # Calculate our middle position
            mid = (left + right) // 2

            # Adjusting pointers based on the results
            if (nums[mid] < nums[right]):
                right = mid
            elif (nums[mid] > nums[right]):
                left = mid + 1

        # Either left or right points at the minimum
        # value, so we return the number there
        return nums[left]

