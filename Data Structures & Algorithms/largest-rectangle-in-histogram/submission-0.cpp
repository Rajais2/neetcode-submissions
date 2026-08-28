class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int maxArea = 0;

        for (int i = 0; i < heights.size(); i++) {
            while (!st.empty() && heights[i] < heights[st.top()]) {
                int curIndex = st.top();
                st.pop();

                int height = heights[curIndex];
                int right = i;
                int left = st.empty() ? -1 : st.top();

                int width = right - left - 1;
                maxArea = max(maxArea, height * width);
            }

            st.push(i);
        }

        while (!st.empty()) {
            int curIndex = st.top();
            st.pop();

            int height = heights[curIndex];
            int right = heights.size();
            int left = st.empty() ? -1 : st.top();

            int width = right - left - 1;
            maxArea = max(maxArea, height * width);
        }

        return maxArea;
    }
};