class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Will hold each final letter
        result = []

        # Keep processing until no more
        while columnNumber > 0:
            # First, subtract 1 from column number
            # to account for Excel's one-indexing
            columnNumber -= 1

            # Obtain the letter's index
            letterIndex = columnNumber % 26

            # Calculate our mapped letter
            letter = chr(ord('A') + letterIndex)

            # Add to our result
            result.append(letter)

            # Update column number
            columnNumber //= 26

        # Return the final result
        return "".join(reversed(result))
        