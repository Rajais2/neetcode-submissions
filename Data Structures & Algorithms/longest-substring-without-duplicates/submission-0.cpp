class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // If the string is empty, return 0
        if (s.size() <= 1) {
            return s.size();
        }
        
        // Creating a hashmap where the character maps with its frequency
        unordered_map<char, int> hashmap;  

        // Creating a variable to hold the max length seen so far
        int maxLength = 0; 

        // Creating a left pointer to help with window resizing
        int leftPointer = 0;

        // Traverse through all individual characters
        for (int i = 0; i < s.size(); i++) {
            // Include the new character by increasing its frequency in the hashmap
            hashmap[s[i]]++;
           
            // Checking for window validity
            while (hashmap[s[i]] > 1) {
                // Shrink the window on the left size
                hashmap[s[leftPointer]]--;
                leftPointer++;
            }

            // Update the max length if necessary
            maxLength = max(maxLength, i - leftPointer + 1);
        }

        // Return the final maximum length
        return maxLength;
    }
};