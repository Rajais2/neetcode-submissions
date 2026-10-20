class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create three pointer to utilize for one pass
        low = 0
        mid = 0
        high = len(nums) - 1

        # Begin the nums traversal!!!!!!!!
        while mid <= high:
            # Act accordingly based on the results
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        # Return the now sorted array
        return nums