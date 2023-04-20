# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        mins = defaultdict(lambda: inf)

        maxes = defaultdict(lambda: -inf)

        

        def dfs(node,level,i):

            if not node: return

            

            mins[level] = min(mins[level],i)

            maxes[level] = max(maxes[level],i)

            

            dfs(node.left,level+1,2*i)

            dfs(node.right,level+1,2*i+1)

            

        dfs(root,1,1)

        

        return max(maxes[level]-mins[level]+1 for level in mins)

            

            
