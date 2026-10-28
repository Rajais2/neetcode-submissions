class Solution:
    def jump(self, nums: List[int]) -> int:
        # Creating to store necessary information
        jumps, currentEnd, farthest = 0, 0, 0

        # Begin scanning the hops...
        for index in range(len(nums) - 1):
            # See the farthest we can jump
            farthest = max(farthest, index + nums[index])

            # Finished scanning the current range
            # so we need a jump and continue the process
            if index == currentEnd:
                jumps += 1
                currentEnd = farthest

        # Returning the number of jumps we need
        return jumps