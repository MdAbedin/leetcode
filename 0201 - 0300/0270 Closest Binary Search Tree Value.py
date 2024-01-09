class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float,start=True) -> int:
        if not root: return (inf,inf)

        ans = (abs(root.val-target),root.val)

        if root.left: ans = min(ans,self.closestValue(root.left,target,False))
        if root.right: ans = min(ans,self.closestValue(root.right,target,False))

        return ans[1] if start else ans
