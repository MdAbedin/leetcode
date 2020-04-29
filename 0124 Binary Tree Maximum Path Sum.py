# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):
        if node is None:
            return 0
        
        left_max = self.helper(node.left)
        right_max = self.helper(node.right)
        cur_max = max(left_max, right_max, left_max+right_max, 0) + node.val
        self.ans = max(self.ans, cur_max)
        
        return max(left_max, right_max, 0)+node.val
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = root.val
        self.helper(root)
        
        return self.ans
