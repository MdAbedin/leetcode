class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev_val = -inf
        ans = inf

        def in_order_traversal(node):
            if not node: return
            nonlocal ans, prev_val

            in_order_traversal(node.left)
            ans = min(ans, node.val-prev_val)
            prev_val = node.val
            in_order_traversal(node.right)

        in_order_traversal(root)

        return ans
