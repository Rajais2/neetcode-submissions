# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Will store the final results
        answer = []
        
        # Creating our DFS function to find
        # all rightmost nodes
        def DFS(node, depth):
            # Stop if we reached the end
            if node is None:
                return

            # Add the node if it's the first node
            # we have found at that depth
            if len(answer) == depth:
                answer.append(node.val)

            # Recurse on the right side first
            # and then on the left
            DFS(node.right, depth + 1)
            DFS(node.left, depth + 1)

        # Begin our recursive exploration
        DFS(root, 0)

        # Return all the rightmost nodes
        # we find
        return answer