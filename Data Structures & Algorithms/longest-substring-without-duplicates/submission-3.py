class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initializing our left pointer and maximum length tracker
        left = 0
        max_length = 0

        # Creating our dictionary to track "seen" characters
        seen = Counter()

        # Utilizing a sliding window approach
        for right in range(len(s)):
            # Obtaining the last character
            char = s[right]

            # Add current character to the window
            # If it doesn't exist, use a zero instead of
            # the seen counter
            seen[char] += 1

            # Shrink window until all characters are unique
            while seen[char] > 1:
                left_char = s[left]
                seen[left_char] -= 1
                left += 1

            # Current window has no duplicates
            max_length = max(max_length, right - left + 1)

        # Returning the maximum length we encountered
        return max_length