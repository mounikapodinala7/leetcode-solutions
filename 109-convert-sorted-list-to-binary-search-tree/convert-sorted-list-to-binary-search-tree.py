class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build_tree(values):
            if not values:
                return None

            mid = len(values) // 2
            node = TreeNode(values[mid])

            node.left = build_tree(values[:mid])
            node.right = build_tree(values[mid + 1:])

            return node

        return build_tree(values)
