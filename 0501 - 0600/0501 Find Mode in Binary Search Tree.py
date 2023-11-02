class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter()

        def solve(node):
            if not node: return
            counts[node.val] += 1
            solve(node.left)
            solve(node.right)

        solve(root)
        mode_count = max(counts.values())

        return [val for val,count in counts.items() if count == mode_count]
