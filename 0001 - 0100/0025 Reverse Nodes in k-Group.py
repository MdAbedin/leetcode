class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = list(takewhile(lambda x:x, accumulate(repeat(head), lambda x,_: x.next)))
        
        for i in range(0,len(nodes),k):
            if i+k-1 < len(nodes): nodes[i:i+k] = reversed(nodes[i:i+k])

        for node1,node2 in pairwise(nodes): node1.next = node2
        nodes[-1].next = None

        return nodes[0]
