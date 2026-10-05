class Solution:
    def countSubstrings(self, s: str) -> int:
        # Resolving base case
        if len(s) == 1:
            return 1
        
        # Create our 2D dp table
        dp = [[False] * len(s) for _ in range(len(s))]

        # Preparring to count the total
        # number of palindromes
        palindromeCount = 0

        # Outer loop: process every substr from shortest to longest
        # Inner loop: for each length, find every valid starting position
        for length in range(1, len(s) + 1):
            for i in range(len(s) - length + 1):
                # Get our ending index
                j = i + length - 1

                # If i and j are equal, we are looking
                # at one character
                if length == 1:
                    dp[i][j] = True
                    palindromeCount += 1
                elif length == 2:
                    # Handling two character potential palindromes
                    if s[i] == s[j]:
                        dp[i][j] = True
                        palindromeCount += 1
                elif length >= 3:
                    # Handling three or more characters
                    # potential palindromes
                    if s[i] == s[j] and dp[i + 1][j - 1] == True:
                        dp[i][j] = True
                        palindromeCount += 1

        # Return the total amount of palindromes
        # we found
        return palindromeCount