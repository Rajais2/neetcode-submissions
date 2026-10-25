# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # First settle if we have no tree
        if root is None:
            return None

        # Recurse based on the value comparsion
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Handle all three cases
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Find the largest node in the left subtree
                current = root.left

                # Keep moving to the right
                while current.right is not None:
                    current = current.right

                # Copy over the value over and delete the original
                # predecessor
                root.val = current.val
                root.left = self.deleteNode(root.left, current.val)

        # In the end, return the updated tree
        return root