class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initializing our two pointers
        left, right = 0, len(heights) - 1

        # Preparring to store the maximum area we found so far
        max_area = 0

        # Performing the two pointer approach
        while left < right:
            # Calculating our total width and height
            width = right - left
            height = min(heights[left], heights[right])

            # Calculating the area with our current dimensions
            area = width * height

            # Updating our max area if necessary
            max_area = max(area, max_area)

            # Checking which pointer to move
            if heights[left] < heights[right]:
                # If the left side is the limiting factor, move
                # the left pointer up
                left += 1
            else:
                # If, on the other hand, the right side is the limiting
                # factor, move it down
                right -= 1

        # Returning the maximum area we calculated
        return max_area