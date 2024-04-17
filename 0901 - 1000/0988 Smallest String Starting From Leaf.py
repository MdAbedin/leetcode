class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def solve(node,s):
            if not node: return "{"
            s = chr(ord("a")+node.val)+s
            return s if not node.left and not node.right else min(solve(node.left,s),solve(node.right,s))

        return solve(root,"")
