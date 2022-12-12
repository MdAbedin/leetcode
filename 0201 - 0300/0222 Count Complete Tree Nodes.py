# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_at_least_size(self, root, size, height):
        while root and height > 1:
            if size%(2**(height-1)) >= 2**(height-2):
                root = root.right
            else:
                root = root.left
                
            height -= 1
            
        return root is not None
    
    def countNodes(self, root: TreeNode) -> int:
        height = 0
        cur = root
        while cur:
            cur = cur.left
            height += 1
            
        l,r = 2**(height-1), 2**height-1
        ans = 0
        
        while l <= r:
            mid = (l+r)//2
            
            if self.is_at_least_size(root, mid, height):
                ans = mid
                l = mid+1
            else:
                r = mid-1
                
        return ans
