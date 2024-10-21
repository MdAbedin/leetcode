class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        carry = 0

        while l1 or l2:
            carry,digit = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry,10)
            ans.append(ListNode(digit))
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: ans.append(ListNode(carry))
        for node1,node2 in pairwise(ans): node1.next = node2

        return ans[0]
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = 0
        
        multiplier = 1
        for node in takewhile(lambda x: x, accumulate(repeat(l1), lambda x,_: x.next)):
            sum_ += multiplier*node.val
            multiplier *= 10
            
        multiplier = 1
        for node in takewhile(lambda x: x, accumulate(repeat(l2), lambda x,_: x.next)):
            sum_ += multiplier*node.val
            multiplier *= 10
            
        if sum_ == 0: return ListNode(0)
        
        ans = ListNode()
        cur = ans
        
        while sum_ > 0:
            sum_, digit = divmod(sum_,10)
            cur.next = ListNode(digit)
            cur = cur.next
        
        return ans.next
