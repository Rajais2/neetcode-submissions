class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Setting up to store the total
        total = 1

        # Checking for negative exponents and 
        # channging accordingly
        if n < 0:
            n = abs(n)
            x = 1 / x

        # Keep performing operations until our
        # exponent becomes zero
        while n != 0:
            # Handling odd exponents
            if n % 2 != 0:
                # We can take one of the multiplers
                # and already multiply it with total
                total *= x
                n -= 1

            # In either case, square x and halve n
            x **= 2
            n //= 2

        # Return the total we accumulate
        return total            