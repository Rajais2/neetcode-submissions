class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strings one character or less in size
        # are always palindromes
        if len(s) <= 1:
            return True
        
        # Setting our left and right pointers
        left, right = 0, len(s) - 1

        # Performing pointer movements!
        while left <= right:
            # Checking if our left pointer is at 
            # an non-alphanumeric character
            while (left <= right and not s[left].isalnum()):
                left += 1

            # Checking if our right pointer is at 
            # an non-alphanumeric character
            while (left <= right and not s[right].isalnum()):
                right -= 1

            # Acting accordingly based on if our characters match
            if left > right:
                return True
            else:
                if (s[left].lower() != s[right].lower()):
                    return False
                else:
                    left += 1
                    right -= 1

        # In the end, we check all characters, so
        # it is a palindrome
        return True