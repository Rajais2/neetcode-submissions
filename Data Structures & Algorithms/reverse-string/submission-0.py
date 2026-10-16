class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Create our two pointers
        left = 0
        right = len(s) - 1

        # Keep moving pointers until they meet
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]

            # Adjust our two pointers
            left += 1
            right -= 1
