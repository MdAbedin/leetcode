# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        bfs = deque()
        bfs.append((root, False))
        
        while bfs:
            cur, is_left = bfs.popleft()
            
            if cur:
                if not cur.left and not cur.right and is_left:
                    ans += cur.val
                    
                bfs.append((cur.left, True))
                bfs.append((cur.right, False))
                
        return ans
