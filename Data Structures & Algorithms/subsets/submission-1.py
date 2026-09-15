class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Setting up to store the global results
        result = []

        # Creating our recursive backtracking function
        def backtrack(index, path):
            # Storing the copy of the current subset
            result.append(path[:])

            # Explore all choices from our index to 
            # full length of our list of nums
            for i in range(index, len(nums)):
                # Add the current number we're on
                path.append(nums[i])

                # Recursively exploring future choices
                backtrack(i + 1, path)

                # Remove/deselect our current number
                path.pop()
                    
        # Begin our recursive backtracking
        backtrack(0, [])

        # Return our final results
        return result
