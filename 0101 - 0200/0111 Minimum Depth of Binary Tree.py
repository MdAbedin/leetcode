class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        bfs = deque([root])
        level = 1

        while bfs:
            for i in range(len(bfs)):
                node = bfs.popleft()

                if not node.left and not node.right: return level
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)

            level += 1
