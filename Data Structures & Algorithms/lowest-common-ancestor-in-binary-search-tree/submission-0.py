# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Resolving base cases
        if root is None:
            return None
        elif root == p or root == q:
            return root

        # Explore both sides to discover information
        leftSide = self.lowestCommonAncestor(root.left, p, q)
        rightSide = self.lowestCommonAncestor(root.right, p, q)

        # Based on the results, we return the 
        # necessary information
        if leftSide is None and rightSide is None:
            return None
        elif leftSide is None and rightSide is not None:
            return rightSide
        elif leftSide is not None and rightSide is None:
            return leftSide
        elif leftSide is not None and rightSide is not None:
            return root