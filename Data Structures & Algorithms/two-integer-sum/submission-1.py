class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating a dict
        seen = {}

        # Traversing the list
        for index, num in enumerate(nums):
            # Getting the complement of our current number
            complement = target - num

            # Checking if we have seen this complement before
            if complement in seen:
                # If so, return the index we're currently on as
                # well as the complement's index
                return [seen[complement], index]
            else:
                # If we haven't seen the complement, simply store the
                # index using the number as a key
                seen[num] = index

        # Returning an empty list just in case
        return []
