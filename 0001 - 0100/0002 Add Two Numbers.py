# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = 0
        
        multiplier = 1
        for node in takewhile(lambda x:x, accumulate(repeat(l1), lambda x,_:x.next)):
            sum_ += multiplier * node.val
            multiplier *= 10
            
        multiplier = 1
        for node in takewhile(lambda x:x, accumulate(repeat(l2), lambda x,_:x.next)):
            sum_ += multiplier * node.val
            multiplier *= 10
            
        if sum_ == 0: return ListNode(0)
        
        ans = ListNode()
        cur = ans
        
        while sum_ > 0:
            sum_, digit = divmod(sum_, 10)
            cur.next = ListNode(digit)
            cur = cur.next
        
        return ans.next
