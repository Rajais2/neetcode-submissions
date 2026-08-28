class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First off, in order to be an anagram, the two
        # strings have to be of the same length
        if len(s) != len(t):
            return False

        # Initializing our dictionary
        counts = {}

        # Looping through each individual character
        # to track frequencies
        for char in s:
            if char in counts:
                # If the character is already present, simply
                # increase its count by one
                counts[char] += 1
            else:
                # Otherwise, set its count to one
                counts[char] = 1

        # Now, we are looping through the other string and
        # subtracting counts
        for char in t:
            if char in counts:
                # Subtract the count if it's seen
                counts[char] -= 1
            else:
                # If we encounter an entirely different letter, then
                # we already know that it is not an anagram
                return False

        # Now checking if all frequencies are at 0
        for freq in counts.values():
            if freq != 0:
                # If any frequency is not 0, it is not an anagram
                return False

        # Otherwise, it is a valid anagram as all frequencies
        # are zero
        return True