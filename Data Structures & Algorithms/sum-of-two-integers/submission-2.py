class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Create a mask to handle negative numbers
        mask = 0xFFFFFFFF
       
        # Here, b is the carry
        while b != 0:
            # Calculate our carry
            carry = (a & b) << 1

            # Update a with XOR
            a = (a ^ b) & mask

            # Assign b to our updated carry
            b = carry

        # Update a if it's above the largest positive integer
        if a > 0x7FFFFFFF:
            a -= 0x100000000

        # Return when there is no more carry left
        return a