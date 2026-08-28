class Solution {
public:
    bool isValid(string s) {
        stack<char> parentheseStack;

        for (int i = 0; i < s.size(); i++) {

            // push opening brackets
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                parentheseStack.push(s[i]);
            }

            // check closing ')'
            else if (s[i] == ')') {
                if (parentheseStack.empty() || parentheseStack.top() != '(') {
                    return false;
                }
                parentheseStack.pop();
            }

            // check closing ']'
            else if (s[i] == ']') {
                if (parentheseStack.empty() || parentheseStack.top() != '[') {
                    return false;
                }
                parentheseStack.pop();
            }

            // check closing '}'
            else if (s[i] == '}') {
                if (parentheseStack.empty() || parentheseStack.top() != '{') {
                    return false;
                }
                parentheseStack.pop();
            }
        }

        // stack must be empty at the end
        return parentheseStack.empty();
    }
};