class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Setting up to store our current and
        # final paths
        curPath = []
        result = []

        # Helps record what numbers we have selected
        visited = [False] * len(nums)

        # Creating our recursive exploration function
        def DFS():
            # Checking if we have a permutation
            if len(curPath) == len(nums):
                result.append(curPath[:])
                return

            # Iterating over all numbers
            for index in range(len(nums)):
                # Checking if we have selected this number already
                if visited[index]:
                    continue

                # Add the number to our current path
                curPath.append(nums[index])
                visited[index] = True

                # Explore that option
                DFS()

                # Undo our choice of selecting that number
                curPath.pop()
                visited[index] = False

        # Call our recursive function
        DFS()

        # Return our final list of permutations
        return result