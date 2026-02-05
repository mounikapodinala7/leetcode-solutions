class Solution:
  def connect(self, root: 'Node') -> 'Node':
    node = root  
    while node:
      dummy = Node(0)  
      needle = dummy
      while node:
        if node.left:  
          needle.next = node.left
          needle = needle.next
        if node.right:  
          needle.next = node.right
          needle = needle.next
        node = node.next
      node = dummy.next  
    return root
        