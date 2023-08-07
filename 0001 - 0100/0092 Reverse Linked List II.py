class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head

        head = ListNode(None,head)
        before = head

        for i in range(left-1): before = before.next

        last = before.next
        cur,nxt = before.next,before.next.next

        for i in range(right-left):
            temp = nxt.next
            nxt.next = cur
            cur,nxt = nxt,temp

        before.next = cur
        last.next = nxt

        return head.next
