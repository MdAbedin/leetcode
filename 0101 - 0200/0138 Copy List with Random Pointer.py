class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None:None}
        node = head

        while node:
            copies[node] = Node(node.val)
            node = node.next

        node = head

        while node:
            copies[node].next = copies[node.next]
            copies[node].random = copies[node.random]
            node = node.next

        return copies[head]
