class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Store the string length
        n = len(s)
        
        # Creating our 2D table
        dp = [[False] * n for _ in range(n)]

        # Will be used in the future to
        # extract the longest palindrome
        startingIdx = 0
        longestLength = 0

        # Mark all one character strings as palindromes
        for i in range(n):
            dp[i][i] = True
            startingIdx = i
            longestLength = 1

        # Check for two character long substrings
        for i in range(n - 1):
            # Get the ending index
            j = i + 1

            # Mark it as True if the two
            # characters match
            if s[i] == s[j]:
                dp[i][j] = True
                startingIdx = i
                longestLength = j - i + 1


        # Now checking for characters longer than
        # two characters
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                # Checking our two main conditions for
                # a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    # Mark it as true
                    dp[i][j] = True

                    # Update our necessary information
                    startingIdx = i
                    longestLength = j - i + 1

        # Return one of the longest 
        # palindromes we found
        return s[startingIdx:startingIdx + longestLength]