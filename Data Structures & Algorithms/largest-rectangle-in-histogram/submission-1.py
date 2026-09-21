class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                curIndex = stack.pop()

                height = heights[curIndex]
                right = i
                left = -1 if not stack else stack[-1]

                width = right - left - 1
                maxArea = max(maxArea, height * width)

            stack.append(i)

        while stack:
            curIndex = stack.pop()

            height = heights[curIndex]
            right = len(heights)
            left = -1 if not stack else stack[-1]

            width = right - left - 1
            maxArea = max(maxArea, height * width)

        return maxArea
