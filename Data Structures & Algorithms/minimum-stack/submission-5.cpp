class MinStack {
public:
    // Creating two different stacks to handle the minimum stack
    stack<int> mainStack;
    stack<int> minStack;

    MinStack() {
    
    }
    
    void push(int val) {
        // Pushing onto the main stack
        mainStack.push(val);

        // Checking if we can push the new value as well to the minimum stack
        if (minStack.empty() || val <= minStack.top()) {
            minStack.push(val);
        } else {
            // Push the new minimum value if needed
            minStack.push(min(val, minStack.top()));
        }
    }
    
    void pop() {
        // Checking if the main stack is empty, so we just return
        if (mainStack.empty()) {
            return;
        }

        // Pop/remove from both stacks
        mainStack.pop();
        minStack.pop();
    }
    
    int top() {
        // Error checking if the main stack is empty
        if (mainStack.empty()) {
            return -1;
        }

        // Returning the top element
        return mainStack.top();
    }
    
    int getMin() {
        // Error checking if the minimum stack is empty
        if (minStack.empty()) {
            return -1;
        }

        // Return the top minimum element
        return minStack.top();
    }
};
