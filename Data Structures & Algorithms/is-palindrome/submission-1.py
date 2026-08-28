class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creating two pointers: one at the beginning, and
        # one at the end
        left, right = 0, len(s) - 1

        # Keep performing operations until we meet in the middle
        while left < right:
            # If the character at our left pointer is not
            # alpha numeric, move our left pointer up
            while left < right and not s[left].isalnum():
                left += 1

            # If the character at our right pointer is not
            # alpha numeric, move our right pointer down
            while left < right and not s[right].isalnum():
                right -= 1

            # If the character at our pointers are not the same, then
            # it is not a palindrome
            if s[left].lower() != s[right].lower():
                return False
            else:
                # Otherwise, move our pointers
                left += 1
                right -= 1

        return True
