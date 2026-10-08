class TimeMap:

    def __init__(self):
        # Creating our map to map key to
        # their values
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # First check if this is a new key
        if key not in self.timeMap:
            # Create the list for that key
            self.timeMap[key] = []

        # Add the new value
        self.timeMap[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # First check if the key exists
        if key not in self.timeMap:
            # If it doesn't exist, return nothing
            return ""

        # Retrieve that key's list of values
        timestamps = self.timeMap[key]

        # Prep for binary search and find the best value
        left = 0
        right = len(timestamps) - 1
        bestVal = ""

        # Perform binary search
        while left <= right:
            # Calculate our mid index
            mid = (left + right) // 2

            # Move pointers accordingly
            if timestamps[mid][0] > timestamp:
                right = mid - 1
            else:
                # Save this as a potential candidate
                bestVal = timestamps[mid][1]
                left = mid + 1

        # Return the best of our efforts the value
        return bestVal