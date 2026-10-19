class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Store the lengths of each string
        indexA = len(a) - 1
        indexB = len(b) - 1

        # Create our carry
        carry = 0

        # Creating our final answer
        additionResult = []

        # Keep performing addition
        while indexA >= 0 or indexB >= 0 or carry:
            # Extract the digit from a if we can
            if indexA >= 0:
                curDigitA = int(a[indexA])
            else:
                curDigitA = 0

            # Extract the digit from b if we can
            if indexB >= 0:
                curDigitB = int(b[indexB])
            else:
                curDigitB = 0

            # Calculate the result digit from addition
            result = curDigitA + curDigitB + carry

            # Get the digit and carry (use two here as
            # we are dealing with binary and not base 10)
            resultDigit = result % 2
            carry = result // 2

            # Append the digit we calculated
            additionResult.append(resultDigit)

            # Decrement both indices
            indexA -= 1
            indexB -= 1

        # Return the final result
        return "".join(reversed([str(d) for d in additionResult]))