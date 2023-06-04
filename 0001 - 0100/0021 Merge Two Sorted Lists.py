class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = sorted(list(takewhile(lambda x: x, accumulate(repeat(list1), lambda x,_: x.next))) + list(takewhile(lambda x: x, accumulate(repeat(list2), lambda x,_: x.next))),key = lambda node: node.val)
        if not nodes: return None
        
        for node1,node2 in pairwise(nodes): node1.next = node2
        nodes[-1].next = None

        return nodes[0]
