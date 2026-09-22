class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # If no intervals, then no removals
        # are required
        if not intervals:
            return 0

        # Sort by the ending times
        intervals.sort(key = lambda interval : interval[1])

        # Recording the ending time for future use
        lastEnd = intervals[0][1]

        # Recording minimum removals
        minimumRemovals = 0

        # Traverse the rest of the intervals
        for index in range(1, len(intervals)):
            if intervals[index][0] < lastEnd:
                # It overlaps so we require a removal
                minimumRemovals += 1
            else:
                # Keep the current interval but update
                # the last ending time to the current one
                lastEnd = intervals[index][1]

        # Return the minimum number of removals required
        return minimumRemovals