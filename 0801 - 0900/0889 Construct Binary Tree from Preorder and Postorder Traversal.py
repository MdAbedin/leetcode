# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, pre_l, pre_r, post_l, post_r):
        if pre_r < pre_l:
            return None
        if pre_r == pre_l:
            return TreeNode(self.pre[pre_l])
    
        root = TreeNode(self.pre[pre_l])
        left_val = self.pre[pre_l+1]
        right_val = self.post[post_r-1]
        
        if left_val == right_val:
            root.left = self.helper(pre_l+1, pre_r, post_l, post_r-1)
        else:
            pre_right_index = self.pre.index(right_val)
            post_left_index = self.post.index(left_val)
            
            root.left = self.helper(pre_l+1, pre_right_index-1, post_l, post_left_index)
            root.right = self.helper(pre_right_index, pre_r, post_left_index+1, post_r-1)
            
        return root
        
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        self.pre, self.post = pre, post
        
        return self.helper(0, len(pre)-1, 0, len(post)-1)
