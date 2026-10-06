class Solution:
    def reverseBits(self, n: int) -> int:
        # Will hold the final number
        result = 0

        # Process up to 32 bits
        for i in range(0, 32):
            # Insert the bit into result and shift
            # it to the left
            result = (result << 1) | (n & 1)

            # Shift n to the right to process
            # a new bit
            n >>= 1

        # Return the final result we achieve
        return result
