class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        // Getting the total gas and cost to see if we can 
        // even make the full circuit
        int totalGas = accumulate(gas.begin(), gas.end(), 0);
        int totalCost = accumulate(cost.begin(), cost.end(), 0);

        // It's impossible if we don't have enough gas
        if (totalGas < totalCost) {
            return -1;
        }

        // Maintain current fuel amounts and candidate index
        int currentFuelAmount = 0, currentCandidateIdx = 0;

        // Go through each station to look for candidates
        for (int i = 0; i < gas.size(); i++) {
            // Get the updated fuel amount at that station
            currentFuelAmount += (gas[i] - cost[i]);

            // If we don't have enough fuel, we know all stations between
            // the starting and ending stations aren't valid candidates
            // So, we update our potential candidate index to be the next one after
            // the station where we failed at
            if (currentFuelAmount < 0) {
                currentFuelAmount = 0;
                currentCandidateIdx = i + 1;
            }
        }

        // Due to our initial check, we know there must be one valid path
        // as it is possible to make a full circuit
        return currentCandidateIdx;
    }
};
