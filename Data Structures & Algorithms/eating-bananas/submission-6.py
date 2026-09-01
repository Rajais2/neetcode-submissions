class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Defining our left and right boundaries
        left, right = 1, max(piles)

        # Setting up to find the minimum speed
        minimumSpeedCan = 0

        # Performing binary search
        while left <= right:
            # Getting our eating speed
            eatingSpeed = (left + right) // 2
            
            # Keeping a counter for how many hours it's been
            totalHoursTaken = 0

            # Go through each pile
            for pile in piles:
                # Calculating the total amount of hours needed
                hoursNeeded = math.ceil(pile / eatingSpeed)
                totalHoursTaken += hoursNeeded

            # Performing various operations depending on results
            if (totalHoursTaken <= h):
                minimumSpeedCan = eatingSpeed
                right = eatingSpeed - 1
            elif (totalHoursTaken > h):
                left = eatingSpeed + 1

        # Returning the minimum speed required
        return minimumSpeedCan