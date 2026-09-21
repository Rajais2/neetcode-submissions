class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Stack stores the INDICES of bars.
        # The heights of these bars are kept in increasing order.
        stack = []

        # Keep track of the largest rectangle we've found.
        maxArea = 0

        # Go through each bar from left to right.
        for i in range(len(heights)):
            # If the current bar is shorter than the bar
            # at the top of the stack, the taller bar can no
            # longer extend to the right.
            while stack and heights[i] < heights[stack[-1]]:
                # Remove the taller bar from the stack.
                curIndex = stack.pop()

                # Get the height of the rectangle we're calculating.
                height = heights[curIndex]

                # The current index is the first bar to the right
                # that is shorter than our current bar.
                right = i

                # After popping, the top of the stack is the first
                # bar to the left that is shorter.
                #
                # If the stack is empty, there is no smaller bar
                # to the left, so we use -1.
                left = -1 if not stack else stack[-1]

                # The rectangle extends from left + 1 to right - 1.
                # Therefore:
                #
                # width = right - left - 1
                width = right - left - 1

                # Calculate the area of this rectangle.
                area = height * width

                # Update the maximum area if this rectangle is larger.
                maxArea = max(maxArea, area)

            # Add the current bar's index to the stack.
            stack.append(i)

        # There may still be bars left in the stack.
        # These bars can extend all the way to the end of the array.
        while stack:

            # Remove the top bar.
            curIndex = stack.pop()

            # Get its height.
            height = heights[curIndex]

            # Since there is no smaller bar to the right,
            # the right boundary is the end of the array.
            right = len(heights)

            # The top of the stack is the first smaller bar
            # to the left.
            #
            # If the stack is empty, there is no smaller bar
            # to the left, so use -1.
            left = -1 if not stack else stack[-1]

            # Calculate the width of the rectangle.
            width = right - left - 1

            # Calculate the area and update the maximum.
            area = height * width
            maxArea = max(maxArea, area)

        # Return the largest rectangle we found.
        return maxArea
