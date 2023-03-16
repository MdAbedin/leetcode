class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(l,r,l2,r2):
            if l > r: return None
            i = inorder.index(postorder[r2])
            l_size = i-l
            return TreeNode(inorder[i], helper(l,i-1,l2,l2+l_size-1), helper(i+1,r,l2+l_size,r2-1))

        return helper(0,len(inorder)-1,0,len(postorder)-1)
