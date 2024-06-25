class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0

        def solve(node):
            if not node: return
            
            nonlocal s

            solve(node.right)
            s += node.val
            node.val = s
            solve(node.left)

        solve(root)

        return root
