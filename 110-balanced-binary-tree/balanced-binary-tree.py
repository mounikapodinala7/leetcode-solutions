class Solution:
    def isBalanced(self, root):
        stack = [(root, False)]
        height = {}
        while stack:
            node, seen = stack.pop()
            if not node:
                continue
            if seen:
                l = height.get(node.left, 0)
                r = height.get(node.right, 0)
                if abs(l - r) > 1:
                    return False
                height[node] = 1 + max(l, r)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return True
