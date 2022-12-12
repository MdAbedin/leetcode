"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
      if not head: return None
      
      dfs = deque([head])
      prev = None
      
      while dfs:
        cur = dfs.pop()
        cur.prev = prev
        prev = cur
        
        if cur.next:
          dfs.append(cur.next)
        if cur.child:
          cur.child.prev = cur
          dfs.append(cur.child)
          
        cur.next = dfs[-1] if dfs else None
        cur.child = None
      
      return head
