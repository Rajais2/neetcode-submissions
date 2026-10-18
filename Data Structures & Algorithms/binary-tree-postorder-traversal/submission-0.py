# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create our final result list
        result = []

        # Create our recursive function
        def DFS(node):
            # Stop if we have no more nodes
            if node is None:
                return

            # First, recurse to the left
            DFS(node.left)

            # Then recurse to the right
            DFS(node.right)

            # Finally, add the root/value
            result.append(node.val)

        # Begin our recursive tracking
        DFS(root)

        # Return our final list
        return result