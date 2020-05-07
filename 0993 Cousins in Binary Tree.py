# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent = y_parent = -1
        x_found = y_found = False
        bfs = deque([root])
        
        while bfs and not x_found and not y_found:
            for i in range(len(bfs)):
                cur = bfs.popleft()
                
                if cur.left:
                    bfs.append(cur.left)

                    if cur.left.val == x:
                        x_found = True
                        x_parent = cur.val

                    if cur.left.val == y:
                        y_found = True
                        y_parent = cur.val

                if cur.right:
                    bfs.append(cur.right)

                    if cur.right.val == x:
                        x_found = True
                        x_parent = cur.val

                    if cur.right.val == y:
                        y_found = True
                        y_parent = cur.val
                        
        return x_found and y_found and x_parent != y_parent
