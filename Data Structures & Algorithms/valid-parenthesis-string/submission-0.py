class Solution:
    def checkValidString(self, s: str) -> bool:
        # Creating minimum and maximum to
        # represent ranges
        minOpen = 0
        maxOpen = 0

        # Begin the string traversal!!!!!!!!!!!
        for character in s:
            # Either increment or decrement our trackers
            # based on the character we encounter
            if character == '(':
                minOpen += 1
                maxOpen += 1
            elif character == ')':
                minOpen -= 1
                maxOpen -= 1
            elif character == '*':
                minOpen -= 1
                maxOpen += 1

            # Clamping minOpen to 0 since we can never
            # have fewer than zero unmatching open
            # parentheses
            if minOpen < 0:
                minOpen = 0

            # If our max for open paranthese ever becomes
            # negative, there is no way to make the string valid
            if maxOpen < 0:
                return False

        # Based on our minimum tracker, it either means
        # a valid interpretation is possible or any
        # interpretation leaves unmatching opening parentheses
        return True if minOpen == 0 else False