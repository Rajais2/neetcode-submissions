class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Defining our left and right pointers
        left, right = 0, len(nums) - 1

        # Keep performing binary search
        while left <= right:
            # Calculate our mid
            mid = (left + right) // 2

            # Checking if our value is the target
            if nums[mid] == target:
                return mid

            # Checking if the left side is sorted
            if nums[left] <= nums[mid]:
                # Target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, the right side is sorted
            else:
                # Target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target is not present
        return -1
