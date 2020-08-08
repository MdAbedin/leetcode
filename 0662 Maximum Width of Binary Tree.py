# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        
        bfs = deque([[root,1]])
        ans = 1
        
        while bfs:
          l,r = -1,-1
          n = len(bfs)
          
          for i in range(n):
            cur, idx = bfs.popleft()
            
            if i == 0: l = idx
            if i == n-1: r = idx
              
            if cur.left: bfs.append([cur.left, idx*2])
            if cur.right: bfs.append([cur.right, idx*2+1])
              
          ans = max(ans, r-l+1)
          
        return ans
