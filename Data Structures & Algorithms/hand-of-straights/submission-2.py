from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If we can't cleanly separate them, then
        # we cannot rearrange the cards correctly
        if len(hand) % groupSize != 0:
            return False

        # Sort our hand
        hand.sort()

        # Count how many of each card we have
        cardFrequencies = Counter(hand)

        # Begin scanning...
        for card in hand:
            # Skip if we have used up this card
            if cardFrequencies[card] == 0:
                continue

            # Using an offset to check for
            # consecutive cards
            offset = 0

            # Checking consecutive cards up to
            # the group size we want
            while offset < groupSize:
                # The card we currently need
                requiredCard = card + offset

                # If we don't have this card available,
                # we can't create the group
                if cardFrequencies[requiredCard] <= 0:
                    return False

                # Use one copy of this card
                cardFrequencies[requiredCard] -= 1

                # Move to the next consecutive card
                offset += 1

        # We successfully grouped all the cards
        return True