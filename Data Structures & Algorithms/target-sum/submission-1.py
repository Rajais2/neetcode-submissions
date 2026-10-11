class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Create a dict to hold all possible sums
        sumWaysDict = {0: 1}

        # Traverse the list!!!!!!!!!!!
        for num in nums:
            # Create a new dict for all possible sums
            # for the current number
            newSumWaysDict = {}

            # Traverse both through all numbers and their
            # total sum ways
            for currentSum, ways in sumWaysDict.items():
                # Update the number of ways to get that
                # sum via addition
                newSumWaysDict[currentSum + num] = newSumWaysDict.get(currentSum + num, 0) + ways

                # Do the same but with subtraction instead
                newSumWaysDict[currentSum - num] = newSumWaysDict.get(currentSum - num, 0) + ways

            # Update our overall dictionary and move on
            # to the next number
            sumWaysDict = newSumWaysDict

        # Return the number of ways to reach the target
        return sumWaysDict.get(target, 0)