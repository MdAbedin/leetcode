class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        def solve(node):
            if not node.left: return node

            ans = solve(node.left)
            node.left.left = node.right
            node.left.right = node
            node.left = node.right = None

            return ans

        return solve(root)
