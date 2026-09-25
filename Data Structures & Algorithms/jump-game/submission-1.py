class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Storing the furthest we can hop
        farthest = 0

        # Begin scanning the list
        for index in range(len(nums)):
            # We have reached the end
            if farthest >= len(nums) - 1:
                return True
            
            # If our scanning is farther than the
            # farthest we can hop, we are stuck
            if index > farthest: 
                return False

            # Update how far we can jump accordingly
            farthest = max(farthest, index + nums[index])

        # Return false as a catch all
        return False
