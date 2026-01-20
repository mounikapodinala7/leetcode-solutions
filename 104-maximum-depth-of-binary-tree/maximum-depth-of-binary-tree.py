class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0
        stack = [(root, 1)]
        while stack:
            node, d = stack.pop()
            if node:
                depth = max(depth, d)
                stack.append((node.left, d + 1))
                stack.append((node.right, d + 1))
        return depth
