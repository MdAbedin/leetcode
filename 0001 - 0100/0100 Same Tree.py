class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (not p and not q) if not p or not q else p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
