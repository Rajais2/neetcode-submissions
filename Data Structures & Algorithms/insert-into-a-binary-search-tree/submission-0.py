# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # First, return the node itself if there
        # is no tree
        if root is None:
            return TreeNode(val)

        # Then we have a tree to traverse
        current = root
        parent = root

        # Begin traversing the tree!!!!!!!!!!!
        while current is not None:
            # Save the parent node in case
            parent = current

            # Move current based on the value
            if val > current.val:
                current = current.right
            else:
                current = current.left

        # Now current should point to None, so 
        # insert and rewire nodes
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        # Now return the tree in the end
        return root