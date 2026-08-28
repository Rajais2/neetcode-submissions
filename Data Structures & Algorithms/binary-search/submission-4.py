class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Setting up our pointers for binary search
        left, right = 0, len(nums) - 1

        # Keep performing binary search
        while left <= right:
            # Calculaing our middle index
            mid = (left + right) // 2

            # Either returning the target's index or moving
            # our pointers based on the results
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # We have searched the entire array, meaning that
        # the target was not found
        return -1