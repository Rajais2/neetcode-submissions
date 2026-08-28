class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned = "";

        for (char character : s) {
            if (isalnum(character)) {
                cleaned += tolower(character);
            }
        }
        
        string original = cleaned;
        reverse(cleaned.begin(), cleaned.end());
        return original == cleaned;
    }
};
