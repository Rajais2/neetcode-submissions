/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/*
class Solution {
public:
    // Helper function to get the height of a current node
    int getHeight(TreeNode* root) {
        // Return nothing as we have reached the end
        if (root == nullptr) {
            return 0;
        }

        // Getting the left and right heights
        int leftHeight = getHeight(root->left);
        int rightHeight = getHeight(root->right);
        
        // Updating our global max diameter
        return 1 + max(leftHeight, rightHeight);
    }

    bool isBalanced(TreeNode* root) {
        // Tree is balanced if the tree is empty
        if (root == nullptr) {
            return true;
        }

        // Get the heights of our nodes
        int leftHeight = getHeight(root->left), rightHeight = getHeight(root->right);

        // Checking if the tree is balanced
        if (abs(leftHeight - rightHeight) > 1) {
            return false;
        }

        // Perform recursive calls on the children
        return isBalanced(root->left) && isBalanced(root->right);
    }
};
*/

class Solution {
public:
    int checkHeight(TreeNode* root) {
        if (!root) return 0;

        int left = checkHeight(root->left);
        if (left == -1) return -1;

        int right = checkHeight(root->right);
        if (right == -1) return -1;

        if (abs(left - right) > 1) return -1;

        return 1 + max(left, right);
    }

    bool isBalanced(TreeNode* root) {
        return checkHeight(root) != -1;
    }
};