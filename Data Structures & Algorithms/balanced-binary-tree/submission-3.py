# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depthFinder(root: Optional[TreeNode]) -> int:
            # If we don't have a node, we have no depth
            if root is None:
                return 0

            # Getting the left and right depths
            leftDepth = depthFinder(root.left)
            rightDepth = depthFinder(root.right)

            # Checking if the right or left side is already unbalanced
            if leftDepth == -1 or rightDepth == -1:
                return -1

            # Checking if we have an unbalanced side
            if (abs(leftDepth - rightDepth) > 1):
                return -1

            # Recurse if otherwise
            return 1 + max(leftDepth, rightDepth)

        # Getting the result of our recursion
        result = depthFinder(root)

        # Depending on our result, the tree is or isn't balanced
        if result == -1:
            return False
        else:
            return True