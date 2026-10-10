class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Create our deque
        dq = deque()

        # Create our final resulting list
        result = []

        # List Traversal Time!!!!!!!!!!
        for i in range(len(nums)):
            # Get our left boundary of our window
            left = i - k + 1

            # Remove old and expired numbers via
            # their indices
            while dq and left > dq[0]:
                dq.popleft()

            # Remove any elements (front) that are smaller
            # than the number we're currently on
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add the current number to the back of our deque
            dq.append(i)

            # If we have processed at least k elements, we
            # have a complete window, so we add the maximum
            # value of the current window to our result
            if i >= k - 1:
                result.append(nums[dq[0]])

        # Return the maximums of each window
        return result