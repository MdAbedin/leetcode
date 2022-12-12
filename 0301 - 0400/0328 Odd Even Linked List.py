# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        last_odd = head
        nxt = head.next
        first_even = head.next
        
        while nxt:
            if nxt.next:
                last_odd.next, nxt.next.next, nxt.next, last_odd, nxt = nxt.next, first_even, nxt.next.next, nxt.next, nxt.next.next
            else:
                break
                
        return head
