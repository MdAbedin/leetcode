class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []

        def iot(node):
            if not node: return

            iot(node.left)
            vals.append(node.val)
            iot(node.right)

        def solve(l,r): return None if l > r else TreeNode(vals[m:=(l+r)//2],solve(l,m-1),solve(m+1,r))

        iot(root)

        return solve(0,len(vals)-1)
