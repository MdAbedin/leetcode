class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,cur = None,head
        while cur: cur.next,prev,cur = prev,cur,cur.next
        return prev
