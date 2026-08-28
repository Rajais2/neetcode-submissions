class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        int num1 = 0, num2 = 0, operation = 0;

        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i] == "+") {
                num1 = st.top();
                st.pop();

                num2 = st.top();
                st.pop();

                operation = num1 + num2;
                st.push(operation);
            } else if (tokens[i] == "-") {
                num1 = st.top();
                st.pop();

                num2 = st.top();
                st.pop();

                operation = num2 - num1;
                st.push(operation);
            } else if (tokens[i] == "*") {
                num1 = st.top();
                st.pop();

                num2 = st.top();
                st.pop();

                operation = num1 * num2;
                st.push(operation);
            } else if (tokens[i] == "/") {
                num1 = st.top();
                st.pop();

                num2 = st.top();
                st.pop();

                operation = num2 / num1;
                st.push(operation);
            } else {
                st.push(stoi(tokens[i]));
            }
        }
        
        return st.top();
    }
};
