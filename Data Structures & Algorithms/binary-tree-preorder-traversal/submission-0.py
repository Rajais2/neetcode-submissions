# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create our final result list
        result = []

        # Create our recursive function
        def DFS(node):
            # Stop if we have no more nodes
            if node is None:
                return

            # First, append the root
            result.append(node.val)

            # Then recurse to the left
            DFS(node.left)

            # Finally recurse to the right
            DFS(node.right)

        # Begin our recursive function
        DFS(root)

        # Return the final result
        return result