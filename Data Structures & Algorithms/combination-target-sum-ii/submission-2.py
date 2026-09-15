class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort our candidates to help deal
        # with duplicates
        candidates.sort()

        # Setting up to store the final result
        result = []

        # Setting up to store the current combination
        combination = []

        # Declaring our recursive DFS function
        def DFS(index, remaining):
            # We have found a combination so add it
            # to our final resulting list
            if remaining == 0:
                result.append(combination.copy())
            
            # No more numbers are available
            if index >= len(candidates):
                return
            
            # Since our list is sorted, we know all
            # future candidates won't work
            if candidates[index] > remaining:
                return

            # Stop if we have exceeded our target
            if remaining < 0:
                return

            # Explore from index onwards
            for i in range(index, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Choose the current number
                combination.append(candidates[i])
                remaining -= candidates[i]

                # Recursively explore the branches
                DFS(i + 1, remaining)

                # Undoing our choice
                combination.pop()
                remaining += candidates[i]
        
        # Begin our recursive journey
        DFS(0, target)

        # Returning the final result
        return result

