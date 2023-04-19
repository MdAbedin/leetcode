class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = -1

        def helper(node):
            if not node: return -1,-1
            cur_ans = 1+helper(node.left)[1],1+helper(node.right)[0]
            self.ans = max(self.ans,max(cur_ans))
            return cur_ans

        helper(root)

        return self.ans
