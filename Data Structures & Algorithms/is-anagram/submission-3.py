class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the two strings aren't the same,
        # then we automatically don't have an anagram
        if len(s) != len(t):
            return False

        # Creating a dictionary to count each individual letter
        counts = {}

        # First going through the first string and counting
        # each instance of each letter
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        # Then go through the second string and decrementing
        # each instance of each letter
        for char in t:
            if char in counts:
                counts[char] -= 1
            else:
                # If the character we're on isn't in the set,
                # then it's automatically not an anagram
                return False

        # Then we go through our dictionary values checking
        # if we have anagrams
        for freq in counts.values():
            if freq != 0:
                return False

        # In the end, we make it so we have anagrams
        return True