class Solution:
    def buildTree(self, preorder, inorder):
        index = 0
        inorder_map = {value: idx for idx, value in enumerate(inorder)}

        def helper(left, right):
            nonlocal index
            if left > right:
                return None

            curr = preorder[index]
            index += 1
            node = TreeNode(curr)

            if left == right:
                return node

            inorder_index = inorder_map[curr]
            node.left = helper(left, inorder_index - 1)
            node.right = helper(inorder_index + 1, right)

            return node

        return helper(0, len(inorder) - 1)