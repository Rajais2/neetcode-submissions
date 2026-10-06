class Solution:
    def hammingWeight(self, n: int) -> int:
        # Implementing a famous algorithm

        # Create a counter
        counter = 0

        # Keep processing as long as
        # we have bits to process
        while n != 0:
            # Increment our counter
            counter += 1

            # Perform the AND bit operation
            n = n & (n - 1)

        # Return our counter of 1's
        return counter