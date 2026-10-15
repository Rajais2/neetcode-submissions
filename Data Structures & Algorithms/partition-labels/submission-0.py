class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Creating a dictionary to store the
        # last seen indices of characters
        lastSeen = {}

        # Creating start and end trackers of the
        # current partition
        start = 0
        end = 0

        # Will eventually store the final answers
        result = []

        # Dictionary building time!!!!!!!!!!!!!
        for i, char in enumerate(s):
            # Update the character's last appearance
            lastSeen[char] = i

        # String traversal time!!!!!!!!!!!!!!!!!!!!!!!!!!!
        for i, char in enumerate(s):
            # Update our end of the current partition
            end = max(end, lastSeen[char])

            # Checking if we have reached the end of
            # the current partition
            if i == end:
                result.append(i - start + 1)

                # As we have reached the end of the current
                # partition, we have to update start
                start = i + 1

        # Return the final lengths we recorded
        return result