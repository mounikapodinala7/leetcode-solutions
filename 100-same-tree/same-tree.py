class Solution:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            a, b = stack.pop()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        return True
