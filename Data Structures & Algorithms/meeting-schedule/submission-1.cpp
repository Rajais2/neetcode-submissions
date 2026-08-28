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
    bool canAttendMeetings(vector<Interval>& intervals) {
        if (intervals.empty()) {
            return true;
        } else if (intervals.size() == 1) {
            return true;
        }
        
        auto compareByStarting = [](const Interval& interval_a, const Interval& interval_b) {
            return interval_a.start < interval_b.start;
        };

        sort(intervals.begin(), intervals.end(), compareByStarting);

        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i].start < intervals[i - 1].end) {
                return false;
            }
        }

        return true;
    }
};
