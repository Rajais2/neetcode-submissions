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

class Solution {
public:
    int DFS(TreeNode* root, int curMaxVal) {
        // Reach the end of the tree so return 0
        if (!root) {
            return 0;
        }
        
        // Seeing if the current node counts as good
        int count = (root->val >= curMaxVal) ? 1 : 0;

        // Updating the current max value if necessary
        int newMax = max(curMaxVal, root->val);

        // Returning the number of contributions and progressing
        // to the left and right subtrees
        return count + DFS(root->left, newMax) + DFS(root->right, newMax);
    }
    
    int goodNodes(TreeNode* root) {
        // If no tree exists, there are no good nodes
        if (!root) {
            return 0;
        }

        return DFS(root, INT_MIN);
    }
};
