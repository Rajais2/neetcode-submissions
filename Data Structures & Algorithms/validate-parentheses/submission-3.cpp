class Solution {
public:
    bool isValid(string s) {
        // Create our stack
        stack<char> parentheseStack;

        // Traverse through each individual character
        for (int i = 0; i < s.size(); i++) {
            // Push the character onto the stack if it's an opening character
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                parentheseStack.push(s[i]);
            } else if (s[i] == ')') {
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