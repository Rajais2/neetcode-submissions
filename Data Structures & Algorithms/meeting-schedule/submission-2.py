"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # If no meetings, then no conflicts
        if not intervals:
            return True

        # Sort by the starting times
        intervals.sort(key = lambda interval : interval.start)

        # Begin traversing the intervals
        for index in range(1, len(intervals)):
            # Extracting information
            current_start, previous_end = intervals[index].start, intervals[index - 1].end

            # Checking for any conflicts
            if current_start < previous_end:
                return False 

        # No conflicts were found
        return True
