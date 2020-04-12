# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node, cur_sum):
        if not node.left and not node.right:
            self.ans += cur_sum*2 + node.val
        
        if node.left:
            self.helper(node.left, cur_sum*2 + node.val)
        if node.right:
            self.helper(node.right, cur_sum*2 + node.val)
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.ans = 0
        self.helper(root, 0)
        return self.ans
