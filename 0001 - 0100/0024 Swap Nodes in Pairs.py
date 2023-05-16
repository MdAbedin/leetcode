class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        nodes = []
        i = 0

        while head:
            if i%2 == 0: nodes.append(head)
            else: nodes.insert(-1,head)
            head = head.next
            i += 1

        for node1,node2 in zip(nodes,nodes[1:]): node1.next = node2
        nodes[-1].next = None

        return nodes[0]
