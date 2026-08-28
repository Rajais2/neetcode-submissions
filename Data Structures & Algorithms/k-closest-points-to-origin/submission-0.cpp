class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Creating a lambda function for our future max heap
        auto dist = [](const vector<int>& point) {
            return point[0] * point[0] + point[1] * point[1];
        };

        auto compareDistance = [&](const vector<int>& a, const vector<int>& b) {
            return dist(a) < dist(b);
        };

        // Creating our max heap which utilizes our lambda function
        // to sort based on distance from the origin
        priority_queue<vector<int>, vector<vector<int>>, decltype(compareDistance)> maxHeap(compareDistance);

        for (auto point : points) {
            maxHeap.push(point);

            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }

        vector<vector<int>> finalResult;

        while (!maxHeap.empty()) {
            finalResult.push_back(maxHeap.top());
            maxHeap.pop();
        }

        return finalResult;
    }
};
