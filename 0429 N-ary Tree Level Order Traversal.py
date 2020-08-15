"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        ans = []
        bfs = deque([root])
        
        while bfs:
            level = []
            
            for i in range(len(bfs)):
                cur = bfs.popleft()
                level.append(cur.val)
                
                for child in cur.children:
                    bfs.append(child)
                    
            ans.append(level)
            
        return ans
