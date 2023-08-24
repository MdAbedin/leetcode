class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        size = 0
        node = root

        while node:
            size *= 2
            size += 1
            node = node.right

        for num in range(1,size+1):
            if bin(num+1).count("1") == 1: continue

            node1 = root

            for bit in bin(num)[3:]:
                if bit == "0": node1 = node1.left
                else: node1 = node1.right

            node2 = root

            for bit in bin(num+1)[3:]:
                if bit == "0": node2 = node2.left
                else: node2 = node2.right

            node1.next = node2

        return root
