class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        list1=[]
        curr=head
        while curr:
            list1.append(curr.val)
            curr=curr.next
        i=left-1
        j=right-1
        list1[i:j+1]=reversed(list1[i:j+1])
        dummy=ListNode(0)
        curr=dummy
        for x in list1:
            curr.next=ListNode(x)
            curr=curr.next
        return dummy.next
        