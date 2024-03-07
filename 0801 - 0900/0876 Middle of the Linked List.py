class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return (nodes := list(takewhile(lambda x: x, accumulate(repeat(head),lambda x,_: x.next))))[len(nodes)//2]
