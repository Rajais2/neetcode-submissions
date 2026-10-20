class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Create counts for dollar bills
        fiveCount = 0
        tenCount = 0

        # Then go through our bills
        for bill in bills:
            # Add to our five dollar count if
            # the customer pays with a five dollar bill
            if bill == 5:
                fiveCount += 1

            # Checking if the user pays with a ten
            # dollar bill
            if bill == 10:
                # We need to have at least one five dollar
                # bill for change
                if fiveCount >= 1:
                    tenCount += 1
                    fiveCount -= 1
                else:
                    return False

            # Now, finally tackling the twenty dollar
            # bill
            if bill == 20:
                if tenCount >= 1 and fiveCount >= 1:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False

        return True