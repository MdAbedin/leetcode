class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head = ListNode(None,head)
        l,r = head,head

        while r.next:
            if r.next.val < x:
                if l == r:
                    l = l.next
                    r = r.next
                else:
                    r_next = r.next
                    r.next = r.next.next

                    r_next.next = l.next
                    l.next = r_next
                    l = l.next
            else:
                r = r.next

        return head.next
