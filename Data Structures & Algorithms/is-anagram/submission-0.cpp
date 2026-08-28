class Solution {
public:
    bool isAnagram(string s, string t) {
        // Automatically false if not the same size
        if (s.size() != t.size()) {
            return false;
        } else if (s.empty() && t.empty()) {
            // Return true as empty strings do count
            return true;
        }

        // Sort both strings
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        // Check the equality between the two strings as now
        // they are both lexicographically sorted
        return s == t;
    }
};
