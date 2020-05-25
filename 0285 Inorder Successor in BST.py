# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ancestor,cur = None, root
        
        while cur != p:
            if cur.val > p.val: ancestor = cur
            cur = cur.left if cur.val > p.val else cur.right
            
        cur = cur.right
        while cur and cur.left:
            cur = cur.left
        
        if not cur and not ancestor:
            return None
        
        if not cur:
            return ancestor
        if not ancestor:
            return cur
        
        
        return cur if cur.val < ancestor.val else ancestor
