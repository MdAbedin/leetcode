class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs = deque([root])
        levels = []
        
        while bfs:
            levels.append(list(bfs))

            for _ in range(len(bfs)):
                node = bfs.popleft()

                if node.left:
                    bfs.append(node.left)
                    bfs.append(node.right)

        for i in range(len(levels)-1):
            if i%2 == 0:
                for i2,node in enumerate(levels[i]):
                    node.left = levels[i+1][~(2*i2)]
                    node.right = levels[i+1][~(2*i2+1)]
            else:
                for i2,node in enumerate(levels[i]):
                    node.right = levels[i+1][~(2*i2)]
                    node.left = levels[i+1][~(2*i2+1)]
            
        return root
