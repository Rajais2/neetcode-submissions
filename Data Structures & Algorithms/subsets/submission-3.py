class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Setting up to store all of our final subsets
        result = []

        # Setting up the current subset we're building
        subset = []

        # Creating our recursive backtracking function
        def dfs(index):
            # If we've reached the end of nums,
            # we've made a decision for every number
            if index >= len(nums):
                # Store a copy of our current subset
                result.append(subset[:])
                return

            # Choice 1: Include the current number
            subset.append(nums[index])

            # Recursively make a decision for the next number
            dfs(index + 1)

            # Backtrack by removing the number we just included
            subset.pop()

            # Choice 2: Don't include the current number
            dfs(index + 1)

        # Begin our backtracking from the first number
        dfs(0)

        # Return all possible subsets
        return result
