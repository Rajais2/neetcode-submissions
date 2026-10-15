class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Set up a candidate value
        candidate = nums[0]

        # Set up a count
        count = 1

        # Traverse the rest of the list
        for i in range(1, len(nums)):
            # If our counter ever reaches zero, then
            # we have a new potential candidate
            if count == 0:
                candidate = nums[i]
            
            # If we encounter the same candidate, increment
            # our counter, else decrement it
            count += (1 if nums[i] == candidate else -1)

        # Return the majority candidate that we find
        return candidate