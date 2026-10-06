class Solution:
    def hammingWeight(self, n: int) -> int:
        # Keep tracks of the number of 1's
        oneCounter = 0
        
        # Keep processing as long as
        # there are bits left
        while n != 0:
            # Inspect the rightmost bit
            if n % 2 == 1:
                # Increment if it's a 1
                oneCounter += 1

            # Shift the bits to the right
            # through division
            n //= 2

        # Return the number of 1's
        # we found
        return oneCounter