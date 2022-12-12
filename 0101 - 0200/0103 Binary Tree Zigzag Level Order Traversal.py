# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
      if not root: return []
      
      bfs = deque([root])
      order = 1
      ans = []
      
      while bfs:
        level = []
        
        for i in range(len(bfs)):
          cur = bfs.popleft()
            
          if order == 1: level.append(cur.val)
          else: level.insert(0, cur.val)
          
          if cur.left: bfs.append(cur.left)
          if cur.right: bfs.append(cur.right)
            
        ans.append(level)
        order *= -1
        
      return ans
