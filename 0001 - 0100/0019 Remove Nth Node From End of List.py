class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = list(takewhile(lambda x: x, accumulate(repeat(head), lambda x,_: x.next)))
        if len(nodes) == 1: return None
        nodes.pop(-n)
        for node1,node2 in pairwise(nodes): node1.next = node2
        if nodes: nodes[-1].next = None

        return nodes[0]
