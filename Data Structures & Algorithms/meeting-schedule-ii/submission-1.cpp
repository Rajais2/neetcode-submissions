/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        // Creating vectors to store all the starting and ending times
        vector<int> allStartingTimes;
        vector<int> allEndingTimes;

        // Obtaining all starting and ending times
        for (auto interval : intervals) {
            allStartingTimes.push_back(interval.start);
            allEndingTimes.push_back(interval.end);
        }   

        // Sorting both vectors
        sort(allStartingTimes.begin(), allStartingTimes.end());
        sort(allEndingTimes.begin(), allEndingTimes.end());

        // Creating our pointers, room counter, and maximum room counter
        int startPointer = 0, endPointer = 0, totalRoomsNeeded = 0, minRooms = 0;

        // Keep processing until all starting/ending times have passed
        while (startPointer < allStartingTimes.size() && endPointer < allEndingTimes.size()) {
            // If there is a conflict, we need a room and increment our start pointer
            if (allStartingTimes[startPointer] < allEndingTimes[endPointer]) {
                totalRoomsNeeded++;
                startPointer++;
            } else {
                // Otherwise, no conflict, so we don't need a room and increment our
                // end pointer
                totalRoomsNeeded--;
                endPointer++;
            }

            // Updating the max number of rooms if necessary
            minRooms = max(minRooms, totalRoomsNeeded);
        }

        // Returning the minimum number of rooms required
        return minRooms;
    }
};
