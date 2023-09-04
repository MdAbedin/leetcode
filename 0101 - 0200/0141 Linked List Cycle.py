class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head

        while True:
            if not fast or not fast.next: return False
            fast = fast.next.next
            slow = slow.next
            if slow == fast: return True
