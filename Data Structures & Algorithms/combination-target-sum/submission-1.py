class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Setting up to store the final answer
        results = []

        # Setting up to store current combinations
        combination = []

        def DFS(index, remaining):
            # If we have reached our target, we have found
            # a valid combination
            if remaining == 0:
                results.append(combination[:])
                return

            # If we have exceeded our target, we need
            # to simply stop
            if remaining < 0:
                return

            # No more numbers are available, so stop
            if index >= len(nums):
                return

            # Select that current number
            combination.append(nums[index])

            # Decrement our remaining target accordingly
            remaining -= nums[index]

            # Recursively explore that decision
            DFS(index, remaining)

            # Remove our last chosen number
            combination.pop()
            remaining += nums[index]

            # Now explore all options by skipping that number
            DFS(index + 1, remaining)

        # Start our recursive journey
        DFS(0, target)

        # Return our final results
        return results