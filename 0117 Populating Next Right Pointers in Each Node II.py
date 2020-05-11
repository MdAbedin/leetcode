"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        bfs = deque([root])
        
        while bfs:
            length = len(bfs)
            for i in range(length):
                cur = bfs.popleft()
                cur.next = bfs[0] if i < length-1 else None
                
                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)
                    
        return root
