class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Creating a set to help check for 
        # consecutive sequences
        sequenceChecker = set()

        # Adding all numbers to our set
        sequenceChecker.update(nums)

        # Setting up to store the longest sequence we find
        longestCount = 0

        # Begin traversing the list
        for num in nums:
            # Checking if it is a new sequence
            if num - 1 not in sequenceChecker:
                # Setting up our main counter
                counter = 1
                
                # Storing the current number we're on
                current = num

                # Checking if it's part of a consecutive sequence
                while current + 1 in sequenceChecker:
                    # Increment our counter
                    counter += 1

                    # Updating our current number
                    current += 1

                # Updating our longest count if necessary
                longestCount = max(longestCount, counter)

        # Returning the longest count we have found
        return longestCount
                