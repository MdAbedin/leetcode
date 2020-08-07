# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
      if not root: return []
      
      ans = []
      bfs = deque([root])

      while bfs:
        level = []

        for i in range(len(bfs)):
          cur = bfs.popleft()
          level.append(cur.val)

          if cur.left: bfs.append(cur.left)
          if cur.right: bfs.append(cur.right)

        ans.append(level)

      return reversed(ans)
