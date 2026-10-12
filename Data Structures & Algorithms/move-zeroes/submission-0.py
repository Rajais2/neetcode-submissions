class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create a slow pointer for writing purposes
        slow = 0

        # Use a fast pointer for reading purposes
        for fast in range(len(nums)):
            # If it is nonzero, swap the values at our
            # two pointers
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

                # Move our slow pointer
                slow += 1

        # Return the in-place modified array
        return nums