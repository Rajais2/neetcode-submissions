class Solution {
public:
    // Creating a mapping of characters to their respective
    // digits (index in the vector)
    vector<string> phoneMap = {
        "",     
        "",     
        "abc",   
        "def",  
        "ghi",  
        "jkl",  
        "mno",  
        "pqrs", 
        "tuv",  
        "wxyz" 
    };

    // Creating a class variable to hold the final result
    vector<string> result;

    void backtrack(string& digits, int index, string& curString) {
        // If we have found a letter combination, add it and stop
        if (index == digits.size()) {
            result.push_back(curString);
            return;
        }

        // Get the current digit and convert it to an index
        int currentDigit = digits[index] - '0';

        // Traverse through all characters respective to that digit
        for (int i = 0; i < phoneMap[currentDigit].size(); i++) {
            // Add the character temporarily
            curString.push_back(phoneMap[currentDigit][i]);

            // Recurse with that new character
            backtrack(digits, index + 1, curString);

            // Undo our last choice
            curString.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        
        // Creating a string to hold the current string for our
        // backtracking purposes
        string curString;

        // Begin the recursion and backtracking
        backtrack(digits, 0, curString);

        // Return the result of all letter combinations
        return result;
    }
};