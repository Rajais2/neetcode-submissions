class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Creating our result array
        result = [0] * len(nums)

        # Setting up to do the prefix product
        prefixProduct = 1

        # Begin our first traversal of the list
        for index, num in enumerate(nums):
            # Store the result first in our resulting array
            result[index] = prefixProduct

            # Then update our running prefix product
            prefixProduct *= num

        # Now we set up to do the suffix product
        suffixProduct = 1

        # Traverse right to left now for suffix
        for index in range(len(nums) - 1, -1, -1):
            # Multiply what we have already with 
            # the current running suffix product
            result[index] *= suffixProduct

            # Update our current running suffix product
            suffixProduct *= nums[index]

        # Return our final result
        return result