class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev :
                self.ans = min(self.ans, root.val - self.prev.val)
            self.prev = root
            inorder(root.right)
            return
        
        inorder(root)
        return self.ans