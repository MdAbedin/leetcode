# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return None
        
        root.left, root.right = self.helper(root.right), self.helper(root.left)
        
        return root
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.helper(root)
