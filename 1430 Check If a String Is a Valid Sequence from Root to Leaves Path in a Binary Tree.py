# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root:
            return not arr
        
        bfs = deque([root])
        level = 0
        
        while bfs:
            for i in range(len(bfs)):
                cur = bfs.popleft()
                
                if level == len(arr)-1:
                    if cur.val == arr[level] and not cur.left and not cur.right:
                        return True
                else:
                    if cur.left and cur.left.val == arr[level+1]:
                        bfs.append(cur.left)
                    if cur.right and cur.right.val == arr[level+1]:
                        bfs.append(cur.right)
                        
            level += 1
            
        return False
