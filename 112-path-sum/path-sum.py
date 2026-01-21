class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, rem):
            if not node:
                return False
            if not node.left and not node.right:
                return rem == node.val
            rem -= node.val
            return dfs(node.left, rem) or dfs(node.right, rem)
        return dfs(root, targetSum)