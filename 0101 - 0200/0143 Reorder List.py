class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None

        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        cur = head
        for i in range(length//2): cur = cur.next
        nxt = cur.next

        while nxt:
            after = nxt.next
            nxt.next = cur
            cur,nxt = nxt,after

        cur1,cur2 = head,cur

        for i in range((length-1)//2):
            cur1_next,cur2_next = cur1.next,cur2.next
            cur1.next,cur2.next = cur2,cur1_next
            cur1,cur2 = cur1_next,cur2_next

        cur2.next = None

        return head
