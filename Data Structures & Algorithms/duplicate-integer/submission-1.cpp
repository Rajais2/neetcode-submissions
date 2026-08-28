class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // Creating a hashmap to assist with checking duplicates
        unordered_map<int, int> duplicateChecker;

        // Traversing through all the numbers
        for (int number : nums) {
            // Attempting to find the position of the current number
            // Wonder if we can use the contain method here as well?
            if (duplicateChecker.contains(number)) {
                // If we have not reached the end, it means it has been seen before
                return true;
            }

            // Marking it as seen
            duplicateChecker[number] = 1;
        }

        // Returning false as all numbers have been examined
        return false;
    }
};