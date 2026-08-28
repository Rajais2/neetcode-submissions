class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Creating our left pointer for the sliding window
        left = 0

        # Creating a dictionary to store frequencies
        frequencies = {}

        # Storing the largest frequency we have seen so far
        largestFreq = 0

        # Storing our final longest answer
        longestLength = 0

        # Utilizing the sliding window approach
        for right in range(len(s)):
            # Obtaining the lastest character and incrementing
            # its frequency
            curCharacter = s[right]
            frequencies[curCharacter] = frequencies.get(curCharacter, 0) + 1

            # Checking if we have a new largest frequency
            largestFreq = max(largestFreq, frequencies[curCharacter])

            # Shrinking Window Condition: if our number of 
            # replacement is greater than k, shrink our window
            while (right - left + 1) - largestFreq > k:
                # Shrink our window
                left_character = s[left]
                frequencies[left_character] -= 1
                left += 1

            # Updating our longest string length if necessary
            longestLength = max(longestLength, right - left + 1)

        # Return the longest string we found
        return longestLength