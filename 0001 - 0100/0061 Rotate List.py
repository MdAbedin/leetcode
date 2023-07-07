class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        
        nodes = list(takewhile(lambda x: x, accumulate(repeat(head), lambda x,_: x.next)))
        nodes = nodes[-(k%len(nodes)):] + nodes[:-(k%len(nodes))]

        for node1,node2 in pairwise(nodes): node1.next = node2
        nodes[-1].next = None

        return nodes[0]
