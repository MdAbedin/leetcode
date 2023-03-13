class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node1,node2):
            if not node1 or not node2: return not node1 and not node2
            return node1.val == node2.val and helper(node1.left,node2.right) and helper(node1.right,node2.left)

        return helper(root.left,root.right)
