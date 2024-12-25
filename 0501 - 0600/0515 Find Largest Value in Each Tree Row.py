class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        bfs = deque([root])

        while bfs:
            ans.append(max(node.val for node in bfs))

            for _ in range(len(bfs)):
                node = bfs.popleft()

                for node2 in [node.left,node.right]:
                    if not node2: continue
                    bfs.append(node2)

        return ans
