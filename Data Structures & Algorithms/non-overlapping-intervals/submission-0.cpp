class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // Making a lambda function to sort by ending times
        auto compareByEnd = [](const vector<int>& interval_a, const vector<int>& interval_b) {
            return interval_a[1] < interval_b[1];
        };

        // Sorting the intervals
        sort(intervals.begin(), intervals.end(), compareByEnd);

        // Getting the earliest ending time
        int currentBoundary = intervals[0][1];

        // Setting up a counter for removed intervals
        int removalCount = 0;

        // Traversing through the rest of the intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If our current interval doesn't conflict, then
            // update the boundary to that interval's ending time
            if (intervals[i][0] >= currentBoundary) {
                currentBoundary = intervals[i][1];
            } else {
                // Otherwise, increment our total removal count
                // as that interval conflicts
                removalCount++;
            }
        }

        // Returning the minimum number of removed intervals
        return removalCount;
    }
};
