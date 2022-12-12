# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
      if p is None or q is None: return p == q
      
      bfs1 = deque([p])
      bfs2 = deque([q])

      while bfs1 and bfs2:
        cur1 = bfs1.popleft()
        cur2 = bfs2.popleft()

        if cur1.val != cur2.val or ((cur1.left is None) != (cur2.left is None)) or ((cur1.right is None) != (cur2.right is None)): return False

        if cur1.left:
          bfs1.append(cur1.left)
          bfs2.append(cur2.left)

        if cur1.right:
          bfs1.append(cur1.right)
          bfs2.append(cur2.right)

      return bfs1 == bfs2
