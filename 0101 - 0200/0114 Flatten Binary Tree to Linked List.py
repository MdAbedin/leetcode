class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def solve(node):
            if not node: return None

            left,right = node.left,node.right
            left_end,right_end = solve(left),solve(right)

            if left:
                node.left = None
                node.right = left
                left_end.right = right

                return right_end if right else left_end
            elif right:
                return right_end
            else:
                return node

        solve(root)
