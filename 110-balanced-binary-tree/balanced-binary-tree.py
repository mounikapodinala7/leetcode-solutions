class Solution:
    def isBalanced(self, mroot: Optional[TreeNode]) -> bool:
            def dfs(root,dpt):
                if not root: return dpt -1
                left = dfs(root.left,dpt+1)
                if left == -1: return -1
                right = dfs(root.right,dpt+1)
                if right == -1: return -1
                if abs(left - right) > 1: return -1
                return max(left, right)
            return  dfs(mroot,1) != -1