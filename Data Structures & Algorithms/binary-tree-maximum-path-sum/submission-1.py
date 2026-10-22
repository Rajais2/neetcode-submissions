# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Creating our global sum
        globalSum = float('-inf')

        # Creating a helper function to find the
        # sums
        def DFS(node):
            nonlocal globalSum
            
            # If we reached the end, stop and
            # contribute nothing
            if node is None:
                return 0

            # Obtain the sums from both left and right
            left_sum = DFS(node.left)
            right_sum = DFS(node.right)

            # Accounting for negative values for the left side
            if left_sum < 0:
                left_sum = 0

            # Accounting for negative values for the right side
            if right_sum < 0:
                right_sum = 0

            globalSum = max(globalSum, node.val + left_sum + right_sum)

            # Returning the best extendable path sum
            return node.val + max(left_sum, right_sum)

        # Invoke our traversal
        DFS(root)

        # Return the maximum path sum
        return globalSum