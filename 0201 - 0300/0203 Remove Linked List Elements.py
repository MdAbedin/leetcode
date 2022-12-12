# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
      while head and head.val == val: head = head.next
        
      cur = head
      prev = None
      
      while cur:
        if cur.val == val: prev.next = cur.next
        else: prev = cur
          
        cur = cur.next
        
      return head
