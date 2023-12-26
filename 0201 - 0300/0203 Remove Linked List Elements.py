class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        nodes = [node for node in takewhile(lambda x: x, accumulate(repeat(head),lambda x,_: x.next)) if node.val != val]
        for node1,node2 in pairwise(nodes): node1.next = node2
        if nodes: nodes[-1].next = None
        
        return None if not nodes else nodes[0]
