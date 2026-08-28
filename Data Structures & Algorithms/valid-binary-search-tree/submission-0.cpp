class Solution {
public:
    bool DFS(TreeNode* root, long long curMin, long long curMax) {
        // Checking if we have an empty node
        if (!root) {
            return true;
        }

        // Checking if the current node's value isn't within bounds
        if (root->val <= curMin || root->val >= curMax) {
            return false;
        }

        // Otherwise, recurse on the left and right children while
        // updating the current minimum and maximum
        return DFS(root->left, curMin, root->val) && DFS(root->right, root->val, curMax);
    }

    bool isValidBST(TreeNode* root) {
        // Call our DFS function to check
        return DFS(root, INT_MIN, INT_MAX);
    }
};