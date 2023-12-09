class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
