class Solution:
    def sumNumbers(self, root: Optional[TreeNode],parent_num=0) -> int:
        if not root: return 0
        num = parent_num*10+root.val
        return num if not root.left and not root.right else self.sumNumbers(root.left,num)+self.sumNumbers(root.right,num)
