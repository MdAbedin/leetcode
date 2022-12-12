# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        num_digits = 0
        cur = head
        while cur:
            num_digits += 1
            cur = cur.next
            
        num_plus_1 = 1
        cur = head
        cur_digit = num_digits
        
        while cur:
            num_plus_1 += cur.val * 10**(cur_digit-1)
            cur_digit -= 1
            cur = cur.next
            
        num_plus_1_str = str(num_plus_1)
        cur = head
        cur_digit = 0
        
        if len(num_plus_1_str) > num_digits:
            head = ListNode(int(num_plus_1_str[0]), head)
            cur = head.next
            cur_digit = 1
            
        while cur_digit < len(num_plus_1_str):
            cur.val = int(num_plus_1_str[cur_digit])
            cur = cur.next
            cur_digit += 1
            
        return head
