class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur_level_first_node = root

        while cur_level_first_node:
            cur_node = cur_level_first_node
            next_level_first_node = None
            next_level_prev_node = None

            while cur_node:
                if cur_node.left:
                    if not next_level_first_node: next_level_first_node = cur_node.left
                    if next_level_prev_node: next_level_prev_node.next = cur_node.left
                    next_level_prev_node = cur_node.left

                if cur_node.right:
                    if not next_level_first_node: next_level_first_node = cur_node.right
                    if next_level_prev_node: next_level_prev_node.next = cur_node.right
                    next_level_prev_node = cur_node.right

                cur_node = cur_node.next

            cur_level_first_node = next_level_first_node

        return root
