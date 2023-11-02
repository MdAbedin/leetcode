class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node: return 0,0,0

            ans,s,c = 0,node.val,1

            for node2 in (node.left,node.right):
                if not node2: continue
                
                ans2,s2,c2 = solve(node2)
                ans += ans2
                s += s2
                c += c2

            return ans + (node.val == s//c),s,c

        return solve(root)[0]
