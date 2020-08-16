# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, l, r):
        if l > r: return None
        
        max_idx = l
        for i in range(l, r+1):
            if self.nums[i] > self.nums[max_idx]:
                max_idx = i
                
        return TreeNode(self.nums[max_idx], self.helper(l, max_idx-1), self.helper(max_idx+1, r))
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        
        return self.helper(0, len(nums)-1)
