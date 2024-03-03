class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = list(takewhile(lambda x: x, accumulate(repeat(head), lambda x,_: x.next))) + [None]
        
        nodes.pop(-(n+1))
        if n != len(nodes): nodes[-(n+1)].next = nodes[-n]

        return nodes[0]
