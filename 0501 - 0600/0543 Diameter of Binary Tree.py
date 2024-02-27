class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node: return 0,0

            left_ans,left_depth = solve(node.left)
            right_ans,right_depth = solve(node.right)

            return max(left_ans,right_ans,left_depth+right_depth),max(left_depth,right_depth)+1
            
        return solve(root)[0]
