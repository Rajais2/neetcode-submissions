class Solution {
public:
    int characterReplacement(string s, int k) {
        // Creating a hashmap to store frequencies of certain characters
        unordered_map<char, int> frequencyMap;

        // Creating necessary tracker variables
        int leftPointer = 0;
        int maxFreq = 0;
        int maxLength = 0;

        // Begin traversing through the string
        for (int rightPointer = 0; rightPointer < s.size(); rightPointer++) {
            // Add the new character by increasing its seen frequency
            frequencyMap[s[rightPointer]]++;

            // Find the new max frequency
            maxFreq = max(maxFreq, frequencyMap[s[rightPointer]]);

            // Shrink the window based on the number of dominant characters
            while ((rightPointer - leftPointer + 1) - maxFreq > k) {
                // Shrink our window and exclude the leftmost character
                frequencyMap[s[leftPointer]]--;
                leftPointer++;
            }

            // Get the new max length
            maxLength = max(maxLength, rightPointer - leftPointer + 1);
        }

        // Return the new maximum length
        return maxLength;
    }
};