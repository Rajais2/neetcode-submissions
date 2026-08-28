class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        // Creating a stack for future use
        stack<int> st;

        // Initializing our final answer vector
        vector<int> finalAnswer(temperatures.size(), 0);

        // Traversing through our temperatures
        for (int i = 0; i < temperatures.size(); i++) {
            // Checking if our stack temperatures are smaller than the current temperature
            while (!st.empty() && temperatures[st.top()] < temperatures[i]) {
                // Getting the position of the top temperature
                int tempPos = st.top();
                st.pop();

                // Update that top temperature's specific position
                finalAnswer[tempPos] = i - tempPos;
            }

            // Otherwise or once done, push that temperature onto our stack
            st.push(i);
        }

        // Return the final answer
        return finalAnswer;
    }
};