class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First sort the array so we can use the
        # two pointer approach
        nums.sort()

        # Preparing to store the final results
        result = []

        # We need the index when traversing the list
        for i in range(len(nums) - 2):
            # If our anchor is the same as the previous, we
            # simply just skip it (avoiding duplicates)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Setting up our two pointers
            left, right = i + 1, len(nums) - 1

            # Now execute the two pointer approach
            while left < right:
                # Calculate our current sum based on our values
                curSum = nums[i] + nums[left] + nums[right]

                # If sum is too small, move our left pointer
                if curSum < 0:
                    left += 1

                # If the sum is too big, move our right pointer
                if curSum > 0:
                    right -= 1

                # If the sum matches 0, add the triplet
                # and adjust
                if curSum == 0:
                    # Add the triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Move our pointers
                    left += 1
                    right -= 1

                    # But we have to check for duplicate values (left pointer)
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1

                    # Now for the right pointer
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1

        # Return the final result
        return result

