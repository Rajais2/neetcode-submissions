"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # No meetings, so rooms needed
        if not intervals:
            return 0

        # Extracting all start times
        starts = [interval.start for interval in intervals]

        # Extracting all ending times
        ends = [interval.end for interval in intervals]

        # Sort both for pointer approach
        starts.sort()
        ends.sort()

        # Recording number of rooms needed
        rooms, maxRooms = 0, 0

        # Creating our two pointers
        start_index, end_index = 0, 0

        # Begin processing all the new meeting starts
        while start_index < len(starts):
            if starts[start_index] < ends[end_index]:
                # Increment rooms and update max rooms accordingly
                rooms += 1
                maxRooms = max(maxRooms, rooms)

                # Move our starting pointer because we have
                # processed one starting time
                start_index += 1
            else:
                # A room is no longer required
                rooms -= 1

                # Move ending pointer up becuase we have
                # processed one ending time
                end_index += 1

        # Returning the most amount of rooms required
        return maxRooms