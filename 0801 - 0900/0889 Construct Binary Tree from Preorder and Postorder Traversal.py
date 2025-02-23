class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None

        ans = TreeNode(preorder[0])
        counts1,counts2 = Counter(),Counter()

        for i,(v1,v2) in enumerate(zip(preorder[1:],postorder[:-1])):
            counts1[v1] += 1
            counts2[v2] += 1

            if counts1 == counts2:
                ans.left = self.constructFromPrePost(preorder[1:i+2],postorder[:i+1])
                ans.right = self.constructFromPrePost(preorder[i+2:],postorder[i+1:-1])
                break

        return ans
