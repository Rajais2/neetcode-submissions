class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If we can't cleanly separate them, then
        # we can not rearrange the cards correctly
        if len(hand) % groupSize != 0:
            return False

        # Sort our hand
        hand.sort()

        # Creating a dictionary to store 
        # card frequencies
        cardFrequencies = {}

        # Begin building freuqencies
        for card in hand:
            if card not in cardFrequencies:
                # We have found a new card
                cardFrequencies[card] = 1
            else:
                # We have seen this card already
                cardFrequencies[card] += 1

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
                # Obtaining the required card we currently need
                requiredCard = card + offset

                # If we have used up all occurrence of that card,
                # then we can't arrange the hand into the group size
                if cardFrequencies.get(requiredCard, 0) <= 0:
                    return False
                
                # Otherwise, we can use the card
                cardFrequencies[requiredCard] -= 1

                # Increase our offset to continue to
                # the next required card
                offset += 1

        # We have gone through all cards and
        # have grouped them successfully
        return True


            
