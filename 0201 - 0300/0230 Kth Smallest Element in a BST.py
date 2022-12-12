# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        iot = deque([root])
        seen = set()
        num_seen = 0
        
        while iot:
            cur = iot.popleft()
            
            if cur.val in seen:
                num_seen += 1
                if num_seen == k:
                    return cur.val
            else:
                if cur.right:
                    iot.appendleft(cur.right)
                    
                iot.appendleft(cur)
                
                if cur.left:
                    iot.appendleft(cur.left)
                    
            seen.add(cur.val)
