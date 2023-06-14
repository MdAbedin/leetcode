class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def solve(node,prev):
            l_max,l_ans = solve(node.left,prev) if node.left else (-inf,inf)
            r_max,r_ans = solve(node.right,node.val) if node.right else (inf,inf)
            return r_max if node.right else node.val,min(l_ans,r_ans,node.val-(l_max if node.left else prev))

        return solve(root,-inf)[1]
