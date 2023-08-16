class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        dfs = [[root,root.val]]

        while dfs:
            node,s = dfs.pop()

            if not node.left and not node.right and s == targetSum: return True

            if node.left: dfs.append([node.left,s+node.left.val])
            if node.right: dfs.append([node.right,s+node.right.val])

        return False
