class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        cur = head

        while cur:
            length += 1
            tail = cur
            cur = cur.next

        cur = head
        for i in range(length//2): cur = cur.next
        prev = None

        while cur:
            next_,cur.next,prev = cur.next,prev,cur
            cur = next_

        cur1,cur2 = head,tail

        for i in range((length-1)//2):
            cur1_next,cur2_next = cur1.next,cur2.next
            cur1.next,cur2.next = cur2,cur1_next
            cur1,cur2 = cur1_next,cur2_next

        return head
