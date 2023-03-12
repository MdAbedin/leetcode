class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [[head.val,id(head),head] for head in lists if head]
        heapify(pq)
        ans = []

        while pq:
            val,_,node = heappop(pq)
            ans.append(val)
            if node.next: heappush(pq,[node.next.val,id(node.next),node.next])

        def make_ll(i): return None if i == len(ans) else ListNode(ans[i],make_ll(i+1))

        return make_ll(0)
