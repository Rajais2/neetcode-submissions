class Solution:
    def trap(self, height: List[int]) -> int:
        # Initializing our two pointers
        left, right = 0, len(height) - 1

        # Initializing the max heights for left and right walls
        left_max, right_max = 0, 0

        # Initializing to hold how much water we can
        water = 0

        # Performing our two pointer approach
        while left < right:
            # Updating the biggest left wall we have seen
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water