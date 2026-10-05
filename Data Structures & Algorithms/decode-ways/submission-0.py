class Solution:
    def numDecodings(self, s: str) -> int:
        # Creating our dynamic table
        dp = [0] * (len(s) + 1)

        # Set our base case
        dp[len(s)] = 1

        # Process the table in reverse
        for i in range(len(s) - 1, -1, -1):
            # Any string with a leading zero is
            # automatically invalid
            if s[i] == '0':
                dp[i] = 0
                continue

            # Now a one digit decoding is possible
            dp[i] = dp[i + 1]

            # Checking for out of bounds
            if i + 1 < len(s):
                # Checking if a two digit decoding is possible
                if 10 <= int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]

        # Return the total number of ways
        return dp[0]
