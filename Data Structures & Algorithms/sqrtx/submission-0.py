class Solution:
    def mySqrt(self, x: int) -> int:
        # Create our two pointers
        left = 0
        right = x

        # Perform binary search
        while left <= right:
            # Calculate our next guess
            mid = (left + right) // 2

            # Store our squared result
            result = mid * mid

            # Act accordingly based on our squared result
            if result == x:
                return mid
            elif result < x:
                left = mid + 1
            elif result > x:
                right = mid - 1

        return right