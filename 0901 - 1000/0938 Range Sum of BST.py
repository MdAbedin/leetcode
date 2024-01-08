class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return 0 if not root else (self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high) + (root.val if low <= root.val <= high else 0))
