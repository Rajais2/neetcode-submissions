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
            # Checking if the left side is controlling the water
            if height[left] <= height[right]:
                # Updating the max height on the left side
                # if necessary
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Otherwise, we can trap up to the amount of
                    # water equal to the height of the left bar minus
                    # the height of the current bar
                    water += left_max - height[left]

                # Move the left pointer up
                left += 1
            else:
                # Here, we know that the right side is
                # controlling the water
                if height[right] >= right_max:
                    # Updating the max height on the right side
                    # if necessary
                    right_max = height[right]
                else:
                    # Otherwise, we can trap up to the amount of
                    # water equal to the height of the right bar minus
                    # the height of the current bar
                    water += right_max - height[right]

                # Move the right pointer down
                right -= 1

        # Return the maximum amount of water we can trap
        return water