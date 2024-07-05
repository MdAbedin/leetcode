class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nodes = list(takewhile(lambda x:x,accumulate(repeat(head),lambda x,_: x.next)))
        return [-1,-1] if len(points := [i for i,a,b,c in zip(count(0),nodes,nodes[1:],nodes[2:]) if a.val > b.val < c.val or a.val < b.val > c.val]) < 2 else [min(map(neg,starmap(sub,pairwise(points)))),points[-1]-points[0]]
