class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        
        while head:
            if head in seen: break
            seen.add(head)
            head = head.next
            
        return head
