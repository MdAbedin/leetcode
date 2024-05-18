class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def solve(v):
            if not v: return 0,0
            ans,coins = map(add,solve(v.left),solve(v.right))
            return ans+abs(coins+v.val-1),coins+v.val-1

        return solve(root)[0]
