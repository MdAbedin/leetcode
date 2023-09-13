class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def solve(node):
            if not node: return

            solve(node.left)
            solve(node.right)
            ans.append(node.val)

        solve(root)

        return ans
