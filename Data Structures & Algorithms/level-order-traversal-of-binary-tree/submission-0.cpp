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
    vector<vector<int>> levelOrder(TreeNode* root) {
        // Checking if we have an empty tree, so return an empty list
        if (root == nullptr) {
            return {};
        }
        
        // Create a queue to perform BFS and push the root node itself
        queue<TreeNode*> nodes;
        nodes.push(root);

        // Setting up to store the number of nodes each level
        int numberOfNodes = 0;

        // Creating a container to hold our final result
        vector<vector<int>> finalResult;

        // Begin the process of popping from the queue until it's empty
        while (!nodes.empty()) {
            // Get the number of nodes to process for each iteration
            numberOfNodes = nodes.size();
            
            // Creating a temporary list to hold the current level nodes
            vector<int> tempNodeVals;

            // Traverse/process the current wave of nodes
            for (int i = 0; i < numberOfNodes; i++) {
                // Popping the first node in our queue
                auto nodeVal = nodes.front();
                nodes.pop();

                // Add the node's value to our temporary list
                tempNodeVals.push_back(nodeVal->val);

                // If the node has a left child, add it
                if (nodeVal->left) {
                    nodes.push(nodeVal->left);
                }

                // If the node has a right child, add it
                if (nodeVal->right) {
                    nodes.push(nodeVal->right);
                }
            }

            // Finally, add the temporary list of node values to our final list
            finalResult.push_back(tempNodeVals);
        }

        // Return the final list containing all nodes processed at each level
        return finalResult;
    }
};