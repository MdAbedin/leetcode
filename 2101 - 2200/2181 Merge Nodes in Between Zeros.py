class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = [ListNode(sum(x.val for x in g)) for k,g in groupby(takewhile(lambda x:x,accumulate(repeat(head),lambda x,_: x.next)),key=lambda x: x.val != 0) if k]
        for a,b in pairwise(ans): a.next = b
        return ans[0]
