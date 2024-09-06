class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        nodes = [node for node in takewhile(lambda x:x, accumulate(repeat(head),lambda x,_:x.next)) if node.val not in nums]
        for node1,node2 in pairwise(nodes): node1.next = node2
        if nodes: nodes[-1].next = None

        return None if not nodes else nodes[0]
