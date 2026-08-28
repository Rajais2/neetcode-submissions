class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // Setting up to store the final result
        vector<vector<int>> result;

        // Setting our loop iterator variable to store our position after each phase ends
        int i = 0;
        
        // First phase: insert all the intervals that are before the new interval
        for (; i < intervals.size() && intervals[i][1] < newInterval[0]; i++) {
            result.push_back(intervals[i]);
        }

        // Second phase: merge the new interval into the current intervals
        for (; i < intervals.size() && intervals[i][0] <= newInterval[1]; i++) {
            // Get the minimum starting starting time
            newInterval[0] = min(newInterval[0], intervals[i][0]);

            // Get the maximum ending time
            newInterval[1] = max(newInterval[1], intervals[i][1]);
        }

        // Insert the newly merged interval
        result.push_back(newInterval);

        // Third phase: push the rest of the intervals back onto the final vector
        for (; i < intervals.size(); i++) {
            result.push_back(intervals[i]);
        }

        // Return the final vector containing the newly inserted vector
        return result;
    }
};