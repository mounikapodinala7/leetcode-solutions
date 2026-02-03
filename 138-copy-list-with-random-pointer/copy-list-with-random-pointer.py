class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Interleave nodes
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate lists
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
            curr = curr.next
            copy_curr = copy_curr.next

        return copy_head