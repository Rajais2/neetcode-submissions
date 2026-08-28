class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Creating a frequency map
        unordered_map<int, int> frequencyMap;

        // Traverse through all numbers and then increment their frequencies
        for (int i = 0; i < nums.size(); i++) {
            frequencyMap[nums[i]]++;
        }

        vector<pair<int, int>> freqVector;

        for (const auto& entry : frequencyMap) {
            freqVector.push_back(entry);
        }

        sort(freqVector.begin(), freqVector.end(),
        [](const pair<int,int>& a, const pair<int,int>& b) {
            return a.second > b.second;
        });

        vector<int> result;

        for (int i = 0; i < k; i++) {
            result.push_back(freqVector[i].first);
        }

        return result;
    }
};
