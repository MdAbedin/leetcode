# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        inorder = []
        iot = deque([root])
        seen = set()
        
        while iot:
            cur = iot.popleft()
            
            if cur in seen:
                inorder.append(cur.val)
            else:
                if cur.right:
                    iot.appendleft(cur.right)
                iot.appendleft(cur)
                if cur.left:
                    iot.appendleft(cur.left)
                    
                seen.add(cur)
           
        for i in range(1,len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
            
        return True
