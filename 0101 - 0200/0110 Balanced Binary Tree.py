class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node: return True,0

            l_ans,l_height = solve(node.left)
            r_ans,r_height = solve(node.right)

            return l_ans and r_ans and abs(l_height-r_height) <= 1, max(l_height,r_height)+1

        return solve(root)[0]
