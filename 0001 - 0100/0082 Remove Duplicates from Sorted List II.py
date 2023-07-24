class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None,head)

        cur = head

        while cur:
            while cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val: cur.next = cur.next.next

            cur = cur.next

        return head.next
