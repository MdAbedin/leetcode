# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(0, head)
        cur = fake_head
        
        while cur.next and cur.next.next:
            node1, node2, node3 = cur.next, cur.next.next, cur.next.next.next
            cur.next = node2
            node2.next = node1
            node1.next = node3
            cur = node1
        
        return fake_head.next
