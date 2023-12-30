class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def not_exists(num):
            node = root

            for bit in bin(num)[3:]:
                if not node: break
                if bit == "0": node = node.left
                else: node = node.right

            return not bool(node)

        return bisect_left(range(1,5*10**4+1),True,key=not_exists)
