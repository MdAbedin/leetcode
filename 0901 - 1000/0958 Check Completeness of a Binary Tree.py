class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        indexes = []

        def helper(node,i):
            if not node: return
            indexes.append(i)
            helper(node.left,i*2+1)
            helper(node.right,i*2+2)

        helper(root,0)

        return sorted(indexes) == list(range(len(indexes)))
