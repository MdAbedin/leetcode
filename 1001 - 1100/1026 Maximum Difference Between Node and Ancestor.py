class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], start = True) -> int:
        if not root: return 0,inf,-inf

        ans,min_val,max_val = 0,root.val,root.val

        for child in [root.left,root.right]:
            ans2,min_val2,max_val2 = self.maxAncestorDiff(child,False)
            ans = max(ans,ans2,root.val-min_val2,max_val2-root.val)
            min_val = min(min_val,min_val2)
            max_val = max(max_val,max_val2)
        
        return ans if start else (ans,min_val,max_val)
