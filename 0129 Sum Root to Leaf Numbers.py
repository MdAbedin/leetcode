# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, total):
        if not root: return
        if not root.left and not root.right:
            self.ans += total + root.val
            return
        
        self.helper(root.left, 10*(total + root.val))
        self.helper(root.right, 10*(total + root.val))
        
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root, 0)
        
        return self.ans
