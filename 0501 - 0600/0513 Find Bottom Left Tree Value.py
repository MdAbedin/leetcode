class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        bfs = deque([root])

        while bfs:
            ans = bfs[0].val

            for i in range(len(bfs)):
                node = bfs.popleft()

                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)

        return ans
