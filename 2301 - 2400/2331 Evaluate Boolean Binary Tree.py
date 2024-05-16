class Solution:
    def evaluateTree(self,root: Optional[TreeNode]) -> bool:return(f:=lambda x:x and[ne,eq,or_,and_][x.val](f(x.left),f(x.right)))(root)
