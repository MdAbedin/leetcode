class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        fake_head = ListNode(None,head)
        psums = [0]
        ps_nodes = {0: fake_head}
        cur = head
        
        while cur:
            ps = psums[-1] + cur.val
            
            if ps in ps_nodes:
                while psums[-1] != ps: ps_nodes.pop(psums.pop())
                ps_nodes[ps].next = cur.next
            else:
                psums.append(ps)
                ps_nodes[ps] = cur

            cur = cur.next
                
        return fake_head.next
