# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Setting up to find the best diameter
        bestDiameter = 0

        # Creating a helper recursive function
        def depthCalc(root: Optional[TreeNode]) -> int:
            # Setting up a nonlocal variable
            nonlocal bestDiameter

            # If the node doesn't exist, return 0
            if root is None:
                return 0

            # Getting the left and right depths
            leftDepth = depthCalc(root.left)
            rightDepth = depthCalc(root.right)

            # Getting the most depthful side
            bestDiameter = max(bestDiameter, leftDepth + rightDepth)

            # Returning that max depth
            return 1 + max(leftDepth, rightDepth)

        # Calling that helper recursive function
        depthCalc(root)

        # Returning our best diamater
        return bestDiameter
