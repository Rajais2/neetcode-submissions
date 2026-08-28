class Solution {
public:
    // Making a global container to hold all results
    vector<vector<string>> result;

    // Making a DFS backtracking where we will explore all possible
    // options, possibly backtrack, and store to our result container
    void backtrack(const string& s, int index, vector<string>& curPath) {
        // If we have matched the original string's length, we have
        // found a viable candidate, so we store it
        if (index == s.size()) {
            result.push_back(curPath);
            return;
        }

        // Loop from the current index to the end of the string to
        // check all possible positions
        for (int end = index; end < s.size(); end++) {
            // Getting the current substring
            string curSubstr = s.substr(index, end - index + 1);

            // If the sub string we extracted is a palindrome, we then
            // explore all possible options from there
            if (isPalindrome(curSubstr)) {
                curPath.push_back(curSubstr);
                backtrack(s, end + 1, curPath);
                curPath.pop_back();
            } else {
                // If it is not a palindrome, simply skip it
                continue;
            }
        }
    }

    // A function that simply checks if a string is a palindrome
    bool isPalindrome(const string& str) {
        return equal(str.begin(), str.begin() + str.size() / 2, str.rbegin());
    }

    vector<vector<string>> partition(string s) {
        vector<string> path;

        backtrack(s, 0, path);

        return result;
    }
};
