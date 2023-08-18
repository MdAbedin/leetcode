class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []

        ans = []
        dfs = [[root,[root.val],root.val]]

        while dfs:
            node,path,s = dfs.pop()

            if not node.left and not node.right and s == targetSum: ans.append(path)
            if node.left: dfs.append([node.left,path+[node.left.val],s+node.left.val])
            if node.right: dfs.append([node.right,path+[node.right.val],s+node.right.val])

        return ans
