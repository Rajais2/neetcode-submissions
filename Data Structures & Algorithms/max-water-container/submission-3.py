class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Setting up our two pointers
        left, right = 0, len(heights) - 1

        # Setting up to store the maximum area we found
        maxArea = 0

        # Performing operations until they overlap
        while left < right:
            # Obtaining necessary information
            height = min(heights[left], heights[right])
            width = right - left

            # Calculate our current area
            area = height * width

            # Update our maximum area if necessary
            maxArea = max(maxArea, area)

            # Checking if the left bar is shorter
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                # Doing the same check with the right bar
                right -= 1
            else:
                right -= 1

        # Return the maximum area we found
        return maxArea