class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Indicates if we have the desired number
        # in each spot
        matching = [False] * len(target)

        # Traverse through each triplet
        for triplet in triplets:
            # Start by assuming the triplet is valid
            valid = True

            # First, check whether the entire triplet is usable
            for index in range(len(triplet)):
                # If any value is greater than its
                # corresponding target value, the entire
                # triplet is unusable
                if triplet[index] > target[index]:
                    valid = False
                    break

            # If the triplet is invalid, move to the next triplet
            if not valid:
                continue

            # The triplet is valid, so now record
            # any positions that match the target
            for index in range(len(triplet)):
                if triplet[index] == target[index]:
                    matching[index] = True

            # Check if we have achieved all three positions
            if all(matching):
                return True

        # We have finished scanning but haven't
        # achieved all three positions
        return False
