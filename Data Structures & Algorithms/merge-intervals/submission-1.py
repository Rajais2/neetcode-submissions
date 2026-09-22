class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Edge case check if we have 
        # no intervals
        if not intervals:
            return []
        
        # Sort the intervals by their
        # starting times
        intervals.sort(key = lambda interval: interval[0])

        # Holds the final answer
        finalResult = []

        # Add the first interval
        finalResult.append(intervals[0].copy())

        # Traverse through the rest of the intervals
        for index in range(1, len(intervals)):
            if finalResult[-1][1] < intervals[index][0]:
                # Simply add it if it doesn't overlap
                finalResult.append(intervals[index])
            else:
                # If it does, simply just merge the lastly
                # inserted interval with the current one
                finalResult[-1][1] = max(intervals[index][1], finalResult[-1][1])

        # Return the final one
        return finalResult