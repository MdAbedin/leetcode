class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        bfs = deque([root])
        ans = []

        while bfs:
            level = []

            for i in range(len(bfs)):
                node = bfs.popleft()
                level.append(node.val)

                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)

            ans.append(level)

        return ans[::-1]
