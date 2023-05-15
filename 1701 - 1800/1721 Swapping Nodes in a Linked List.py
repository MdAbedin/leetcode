class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        nodes[k-1],nodes[~(k-1)] = nodes[~(k-1)],nodes[k-1]

        for node1,node2 in zip(nodes,nodes[1:]): node1.next = node2

        nodes[-1].next = None

        return nodes[0]
