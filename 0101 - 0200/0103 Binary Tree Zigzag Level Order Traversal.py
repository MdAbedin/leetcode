class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        ans = []
        bfs = deque([root])
        reverse = False

        while bfs:
            level = [node.val for node in bfs]
            if reverse: level.reverse()
            ans.append(level)
            reverse = not reverse

            for i in range(len(bfs)):
                cur = bfs.popleft()

                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)

        return ans
