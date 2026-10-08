from typing import List


class Solution:

    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        # First, we need to make nums1 the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Set up our binary search boundaries
        left = 0
        right = len(nums1)

        # Calculating our divider
        half = (len(nums1) + len(nums2) + 1) // 2

        # Perform binary search
        while left <= right:
            # Calculate mid and the other partition
            mid = (left + right) // 2
            partition2 = half - mid

            # Get the left boundary values
            if mid > 0:
                nums1_left = nums1[mid - 1]
            else:
                nums1_left = float("-inf")

            if mid < len(nums1):
                nums1_right = nums1[mid]
            else:
                nums1_right = float("inf")

            # Get the right boundary values
            if partition2 > 0:
                nums2_left = nums2[partition2 - 1]
            else:
                nums2_left = float("-inf")

            if partition2 < len(nums2):
                nums2_right = nums2[partition2]
            else:
                nums2_right = float("inf")

            # Check if partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # If total length is odd
                if (len(nums1) + len(nums2)) % 2 != 0:
                    return float(max(nums1_left, nums2_left))
                # If total length is even
                return (
                    max(nums1_left, nums2_left) + min(nums1_right, nums2_right)
                ) / 2.0

            # Too far right in nums1, move left
            elif nums1_left > nums2_right:
                right = mid - 1

            # Too far left in nums1, move right
            else:
                left = mid + 1

        return 0.0