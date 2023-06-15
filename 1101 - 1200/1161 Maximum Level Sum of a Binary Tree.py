class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        max_sum = -inf
        ans = None
        bfs = deque([root])
        
        while bfs:
            cur_sum = sum(node.val for node in bfs)
            if cur_sum > max_sum:
                max_sum = cur_sum
                ans = level
                
            for i in range(len(bfs)):
                cur = bfs.popleft()
                
                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)
                    
            level += 1
                    
        return ans

      
