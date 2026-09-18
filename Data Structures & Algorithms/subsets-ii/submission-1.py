class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to help handle
        # with duplicates
        nums.sort()
        
        # Creating our final and current lists
        curPath, result = [], []

        # Creating our recursive function
        def DFS(start):
            # Adding the current path as a valid result
            result.append(curPath.copy())

            # Iterate from our starting position and onwards
            for index in range(start, len(nums)):
                # Checking for duplicates
                if index > start and nums[index] == nums[index - 1]:
                    continue

                # Choose our current number
                curPath.append(nums[index])

                # Recursively explore that decision
                DFS(index + 1)

                # Undo our decision
                curPath.pop()

        # Call our recursive function
        DFS(0)

        # Return our final resulting list
        return result