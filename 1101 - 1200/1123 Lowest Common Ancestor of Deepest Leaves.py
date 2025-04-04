class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = [-1,-1,-1,-1,None]

        def solve(node,d):
            nonlocal ans

            d1 = d if not node.left else solve(node.left,d+1)
            d2 = d if not node.right else solve(node.right,d+1)

            ans = max(ans,[d1,d2,-d,id(node),node])

            return max(d1,d2)

        solve(root,0)

        return ans[-1]
