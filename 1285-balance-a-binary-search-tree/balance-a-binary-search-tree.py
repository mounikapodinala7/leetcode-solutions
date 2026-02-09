class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            a.append(root)
            inorder(root.right)
        inorder(root)

        def makeBST(l, r):
            if l > r: return None
            mid = (l+r)//2
            a[mid].left = makeBST(l, mid - 1)
            a[mid].right = makeBST(mid + 1, r)
            return a[mid]
        return makeBST(0, len(a)-1)