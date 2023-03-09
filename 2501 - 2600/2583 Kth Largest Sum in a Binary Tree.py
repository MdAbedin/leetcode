class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = []
        bfs = deque([root])
        
        while bfs:
            levels.append(sum(node.val for node in bfs))
            
            for i in range(len(bfs)):
                cur = bfs.popleft()
                
                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)
                    
        if len(levels) < k: return -1
        
        return sorted(levels,reverse=True)[k-1]
