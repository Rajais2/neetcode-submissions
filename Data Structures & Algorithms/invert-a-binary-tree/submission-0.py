# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Checking if we have a tree
        if root is None:
            return None

        # Temporarily store one of the children
        tempChild = root.left

        # Swap the children
        root.left = root.right
        root.right = tempChild

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Returning the root
        return root