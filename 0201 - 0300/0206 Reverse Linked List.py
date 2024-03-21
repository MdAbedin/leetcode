class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,cur = None,head

        while cur:
            next_,cur.next,prev = cur.next,prev,cur
            cur = next_

        return prev
