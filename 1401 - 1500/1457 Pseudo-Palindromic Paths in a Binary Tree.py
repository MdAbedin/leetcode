class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], counts = Counter()) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1 if sum(c%2 for c in (counts+Counter({root.val:1})).values()) <= 1 else 0
        return sum(self.pseudoPalindromicPaths(child,counts+Counter({root.val:1})) for child in [root.left,root.right])
