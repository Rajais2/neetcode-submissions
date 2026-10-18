# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create our final result list
        result = []

        # Create our recursive function for the traversal
        def DFS(node):
            # Stop if we have no more nodes
            if node is None:
                return

            # First, recurse left
            DFS(node.left)

            # Then append
            result.append(node.val)

            # Finally, recurse right
            DFS(node.right)

        # Begin our DFS function
        DFS(root)

        # Return our final result
        return result