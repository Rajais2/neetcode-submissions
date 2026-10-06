# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # If the tree doesn't exist, we
        # just return 0
        if root is None:
            return 0
       
        # Creating a counter to help
        # find the kth smallest value
        counter = 0

        # Creating our inorder traversal function
        def inOrderTraversal(node):
            if node is None:
                return None
            
            nonlocal counter
            
            # Traverse left
            leftResult = inOrderTraversal(node.left)

            if leftResult is not None:
                return leftResult

            # Visit the node so we increment
            # the counter
            counter += 1

            # Checking if we found the answer
            if counter == k:
                return node.val

            # Traverse now to the right
            return inOrderTraversal(node.right)

        # Begin our recursive journey 
        return inOrderTraversal(root)

