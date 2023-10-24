class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        bfs = deque([root])

        while bfs:
            ans.append(max(node.val for node in bfs))

            for i in range(len(bfs)):
                cur = bfs.popleft()

                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)

        return ans
