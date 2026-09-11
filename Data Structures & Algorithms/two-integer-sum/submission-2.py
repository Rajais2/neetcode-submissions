class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating a dictionary
        numTracker = {}

        # Begin traversing the list of numbers
        for index, num in enumerate(nums):
            # Getting the complement
            complement = target - num

            # Checking if we have seen this complement already
            if complement in numTracker:
                return [numTracker[complement], index]
            else:
                # If we haven't, add it to our dictionary
                numTracker[num] = index

        # If we didn't find a pair, simply return nothing
        return []