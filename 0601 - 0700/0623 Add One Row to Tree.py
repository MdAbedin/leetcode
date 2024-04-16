class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val,root)

        bfs = deque([root])

        for i in range(depth-2):
            for i2 in range(len(bfs)):
                node = bfs.popleft()
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)

        for node in bfs:
            node.left = TreeNode(val,node.left)
            node.right = TreeNode(val,None,node.right)

        return root
