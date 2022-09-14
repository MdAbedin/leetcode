class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        dfs = [root]
        start_node = None
        
        while dfs:
            cur = dfs.pop()
            
            if cur.val == startValue: start_node = cur
            
            if cur.left:
                dfs.append(cur.left)
                parents[cur.left] = cur
                
            if cur.right:
                dfs.append(cur.right)
                parents[cur.right] = cur
                
        moves = {}
        dfs = [start_node]
        seen = {start_node}
        
        while dfs:
            cur = dfs.pop()
            
            if cur.val == destValue:
                ans = []
                
                while cur != start_node:
                    ans.append(moves[cur][1])
                    cur = moves[cur][0]
                    
                return "".join(ans[::-1])
            
            if cur in parents and parents[cur] not in seen:
                seen.add(parents[cur])
                dfs.append(parents[cur])
                moves[parents[cur]] = [cur, "U"]
                
            if cur.left and cur.left not in seen:
                seen.add(cur.left)
                dfs.append(cur.left)
                moves[cur.left] = [cur, "L"]
                
            if cur.right and cur.right not in seen:
                seen.add(cur.right)
                dfs.append(cur.right)
                moves[cur.right] = [cur, "R"]
