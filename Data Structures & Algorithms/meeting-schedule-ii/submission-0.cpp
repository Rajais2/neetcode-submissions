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
        vector<int> allStartingTimes;
        vector<int> allEndingTimes;

        for (auto interval : intervals) {
            allStartingTimes.push_back(interval.start);
            allEndingTimes.push_back(interval.end);
        }   

        sort(allStartingTimes.begin(), allStartingTimes.end());
        sort(allEndingTimes.begin(), allEndingTimes.end());

        int startPointer = 0, endPointer = 0, totalRoomsNeeded = 0, maxRooms = 0;

        while (startPointer < allStartingTimes.size() && endPointer < allEndingTimes.size()) {
            if (allStartingTimes[startPointer] < allEndingTimes[endPointer]) {
                totalRoomsNeeded++;
                startPointer++;
            } else {
                totalRoomsNeeded--;
                endPointer++;
            }

            maxRooms = max(maxRooms, totalRoomsNeeded);
        }

        return maxRooms;
    }
};
