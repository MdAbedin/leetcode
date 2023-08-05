class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(s,e): return [None] if s > e else [TreeNode(root,l,r) for root in range(s,e+1) for l,r in product(solve(s,root-1),solve(root+1,e))]
        return solve(1,n)
