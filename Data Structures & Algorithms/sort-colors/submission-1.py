class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create a counter for all numbers
        numCount = Counter(nums)

        # Create a write pointer
        write = 0

        # Begin the overwriting process!!!!!!!
        for color in range(3):
            for _ in range(numCount[color]):
                # Overwrite the array with the color
                nums[write] = color

                # Advance our write pointer
                write += 1

        # Return the now sorted array
        return nums