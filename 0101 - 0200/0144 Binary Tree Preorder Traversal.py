class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        dfs = [root]
        ans = []

        while dfs:
            node = dfs.pop()
            ans.append(node.val)

            if node.right: dfs.append(node.right)
            if node.left: dfs.append(node.left)

        return ans
