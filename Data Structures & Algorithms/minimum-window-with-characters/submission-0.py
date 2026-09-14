class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if len(t) == 0:
            return ""
        if len(t) > len(s):
            return ""

        # Frequency requirements for t
        subStrFrequencies = {}

        # Calculating the frequencies in t
        for character in t:
            subStrFrequencies[character] = (
                subStrFrequencies.get(character, 0) + 1
            )

        # Number of unique characters we need to satisfy
        required = len(subStrFrequencies)

        # Sliding window state
        windowFrequencies = {}
        formed = 0
        left = 0

        # Best window found so far
        minWindowLength = float("inf")
        bestStart = 0

        # Expand window with right
        for right in range(len(s)):
            curCharacter = s[right]

            # Add character to window
            windowFrequencies[curCharacter] = (
                windowFrequencies.get(curCharacter, 0) + 1
            )

            # Check if this character just satisfied a requirement
            if curCharacter in subStrFrequencies:
                if windowFrequencies[curCharacter] == subStrFrequencies[curCharacter]:
                    formed += 1

            # Shrink window while it is valid
            while formed == required:
                curWindowLength = right - left + 1

                # Save this window only if it is smaller
                if curWindowLength < minWindowLength:
                    minWindowLength = curWindowLength
                    bestStart = left

                # Remove leftmost character
                leavingCharacter = s[left]
                windowFrequencies[leavingCharacter] -= 1

                # Check if removing it made the window invalid
                if leavingCharacter in subStrFrequencies:
                    if windowFrequencies[leavingCharacter] < subStrFrequencies[leavingCharacter]:
                        formed -= 1

                left += 1

        # No valid window was found
        if minWindowLength == float("inf"):
            return ""

        return s[bestStart:bestStart + minWindowLength]
