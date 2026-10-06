class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Map each value to its index in inorder
        inorder_map = {value: index for index, value in enumerate(inorder)}

        preorder_index = 0

        def buildSubtree(left, right):
            nonlocal preorder_index

            # No elements in this subtree
            if left > right:
                return None

            # The next preorder value is always the root
            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            # Find root's position in inorder in O(1)
            root_index = inorder_map[root_value]

            # Build left subtree
            root.left = buildSubtree(left, root_index - 1)

            # Build right subtree
            root.right = buildSubtree(root_index + 1, right)

            return root

        return buildSubtree(0, len(inorder) - 1)