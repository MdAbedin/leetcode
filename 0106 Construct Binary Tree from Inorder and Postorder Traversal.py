# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, l1, r1, l2, r2):
        if l1 > r1: return None
        
        mid = self.postorder[r2]
        mid_idx = self.inorder.index(mid)
        left_size = mid_idx - l1
        
        return TreeNode(mid, self.helper(l1, l1+left_size-1, l2, l2+left_size-1), self.helper(mid_idx+1, r1, l2+left_size, r2-1))
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.postorder = postorder
        
        return self.helper(0, len(inorder)-1, 0, len(postorder)-1)
