class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # No intervals, no queries can be done
        if not intervals:
            return [-1] * len(queries)

        # Sort our intervals by their starting times
        intervals.sort()

        # Setting up an interval pointer
        interval_index = 0

        # Sorting our queries while keeping what 
        # interval they belong to
        sortedQueries = sorted((query, index) for index, query in enumerate(queries))

        # Creating a results array to hold the final answers
        result = [-1] * len(queries)

        # Creating a minimum heap
        minHeap = []

        # Traverse each query to process them and add to min heap
        for query, query_index in sortedQueries:
            # Checking the current query against intervals
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                # Getting the interval's length
                start, end = intervals[interval_index]
                length = end - start + 1

                # Push the interval's length and its ending time onto our min heap
                heapq.heappush(minHeap, (length, end))

                # Increment our interval pointer since 
                # we have processed an interval
                interval_index += 1

            # Removing all expired intervals against the query
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            if minHeap:
                result[query_index] = minHeap[0][0]


        return result