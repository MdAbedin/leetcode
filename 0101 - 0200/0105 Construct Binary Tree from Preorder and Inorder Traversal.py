class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solve(l1,r1,l2,r2):
            if l1 > r1: return None

            left_len = inorder.index(preorder[l1],l2)-l2
            right_len = r1-l1-left_len

            return TreeNode(preorder[l1], solve(l1+1,l1+left_len,l2,l2+left_len-1), solve(r1-right_len+1,r1,r2-right_len+1,r2))

        return solve(0,len(preorder)-1,0,len(inorder)-1)
