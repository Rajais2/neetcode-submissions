class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to map numbers
        # to their indices
        numIndexMap = {}

        # Traverse the list!!!!!!
        for i, num in enumerate(nums):
            # Checking if the number has appeared before
            if num in numIndexMap:
                # If it is, calculate the distance
                dist = abs(i - numIndexMap[num])

                # Check the distance to see if we
                # have found a valid result
                if dist <= k:
                    return True

            # If we didn't find a valid result, update the
            # number's index
            numIndexMap[num] = i

        # If we have traversed all the numbers, then
        # we didn't find anything
        return False