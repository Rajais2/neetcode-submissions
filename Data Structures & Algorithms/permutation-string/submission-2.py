class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge cases
        if len(s1) == 0:
            return True
        if len(s1) > len(s2):
            return False

        # Frequency array for s1
        s1Frequencies = [0] * 26

        # Build those frequencies in the smaller string
        for character in s1:
            charIndex = ord(character) - ord('a')
            s1Frequencies[charIndex] += 1

        # Frequency array for the first window of s2
        windowFrequencies = [0] * 26

        # Build frequencies up to the length of the smaller string
        for i in range(len(s1)):
            charIndex = ord(s2[i]) - ord('a')
            windowFrequencies[charIndex] += 1

        # Check the first window
        if s1Frequencies == windowFrequencies:
            return True

        # Slide the window through the rest of s2
        for right in range(len(s1), len(s2)):
            # Remove the character leaving the window
            leavingCharIndex = ord(s2[right - len(s1)]) - ord('a')
            windowFrequencies[leavingCharIndex] -= 1

            # Add the character entering the window
            enteringCharIndex = ord(s2[right]) - ord('a')
            windowFrequencies[enteringCharIndex] += 1

            # Check if this window is a permutation of s1
            if s1Frequencies == windowFrequencies:
                return True

        # We have ran through the entire string, so
        # no permutation was found
        return False
