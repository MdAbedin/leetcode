class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_nodes = set(takewhile(lambda x: x,accumulate(repeat(headA),lambda x,_: x.next)))
        b_nodes = list(takewhile(lambda x: x,accumulate(repeat(headB),lambda x,_: x.next)))
        return None if not a_nodes & set(b_nodes) else list(filter(a_nodes.__contains__,b_nodes))[0]
