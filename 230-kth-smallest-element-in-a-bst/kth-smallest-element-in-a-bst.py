class Solution:
    def kthSmallest(self, r: Optional[TreeNode], k: int) -> int:
        return (f:=lambda n:n and f(n.left)+[n.val]+f(n.right) or [])(r)[k-1]