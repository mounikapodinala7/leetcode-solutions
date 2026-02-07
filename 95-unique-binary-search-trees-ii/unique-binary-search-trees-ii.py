class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]

            trees = []
            for i in range(start, end + 1):
                left = build(start, i - 1)
                right = build(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees

        return build(1, n)