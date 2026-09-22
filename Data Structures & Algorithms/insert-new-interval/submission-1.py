class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Creating a final list to hold our answer
        finalResult = []
        
        # Setting a flag for if we have
        # intervals that are all before the new
        # interval
        afterIntervalFlag = False

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
                
                # Turn on our flag and stop looping
                afterIntervalFlag = True
                break
            else:
                # Merge our two intervals into one
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # Append the new interval if all
        # intervals were before the new interval
        if not afterIntervalFlag:
            finalResult.append(newInterval)

        # Return our final result
        return finalResult