
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Create a list to eventually hold the final answer
        result = [0] * (len(num1) + len(num2))

        # Traverse through each digit in our first number,
        # starting from right to left
        for i in range(len(num1) - 1, -1, -1):
            # Convert the current digit we're on
            digit = int(num1[i])

            # Traverse through each digit in our second number,
            # also starting from right to left
            for j in range(len(num2) - 1, -1, -1):
                # Convert the current digit we're on
                # in the second number
                secondDigit = int(num2[j])

                # Calculate our product and account for
                # the existing value at the ones-digit position
                product = digit * secondDigit
                existingVal = result[i + j + 1]
                total = product + existingVal

                # Extract necessary information
                onesDigit = total % 10
                carry = total // 10

                # Update/store necessary positions
                result[i + j + 1] = onesDigit
                result[i + j] += carry

        # Convert our list to a string
        finalNum = "".join([str(d) for d in result]).lstrip("0")

        # If our final result is all zeros, return
        # 0 as our final, otherwise return the result
        if finalNum == "":
            return "0"
        else:
            return finalNum
