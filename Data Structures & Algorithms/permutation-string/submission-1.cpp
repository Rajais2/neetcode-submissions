class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }
        
        // Creating a vector to represent character frequencies
        vector<int> s1Freq(26, 0);
        vector<int> windowFreq(26, 0);

        for (int i = 0; i < s1.size(); i++) {
            int charIndex = s1[i] - 'a';
            s1Freq[charIndex]++;
        }

        for (int i = 0; i < s1.size(); i++) {
            int charIndex = s2[i] - 'a';
            windowFreq[charIndex]++;
        }

        if (s1Freq == windowFreq) {
            return true;
        }

        for (int i = s1.size(); i < s2.size(); i++) {
            int leavingCharIndex = s2[i - s1.size()] - 'a';
            windowFreq[leavingCharIndex]--;

            int enteringCharIndex = s2[i] - 'a';
            windowFreq[enteringCharIndex]++;

            if (s1Freq == windowFreq) {
                return true;
            }   
        }

        return false;
    }
};
