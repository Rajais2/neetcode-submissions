class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Creating a final list to hold our answer
        finalResult = []

        # Traverse through each individual interval
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                # Add the interval if it's before the
                # new interval
                finalResult.append(interval)

            elif interval[0] > newInterval[1]:
                # Append the new interval and everything afterwards
                finalResult.append(newInterval)
                finalResult.extend(intervals[index:])

                # Stop looping
                break

            else:
                # Merge our two intervals into one
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        else:
            # If we never hit break, the new interval
            # belongs at the end
            finalResult.append(newInterval)

        # Return the final result
        return finalResult