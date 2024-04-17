class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        row = [root := TreeNode(None,root)]
        for i in range(depth-1): row = [child for node in row for child in (node.left, node.right) if child]

        for node in row:
            node.left = TreeNode(val,node.left)
            node.right = TreeNode(val,None,node.right)

        return root.left
