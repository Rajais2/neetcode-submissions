class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>, less<int>> maxHeap;

        for (auto stone : stones) {
            maxHeap.push(stone);
        }

        while (maxHeap.size() >= 2) {
            auto firstStone = maxHeap.top();
            maxHeap.pop();

            auto secondStone = maxHeap.top();
            maxHeap.pop();

            if (firstStone != secondStone) {
                maxHeap.push(abs(secondStone - firstStone));
            }
        }

        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};
