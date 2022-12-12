# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root or not root.val:
            return []
        
        lefts, rights = deque(), deque()
        lefts.append(root)
        ans = []
        
        while lefts or rights:
            if lefts:
                cur = lefts.popleft()

                if cur:
                    ans.append(cur.val)

                    if cur.left:
                        lefts.appendleft(cur.left)
                    if cur.right:
                        rights.appendleft(cur.right)
            else:
                cur = rights.popleft()
                
                if cur:
                    ans.append(cur.val)
                    
                    if cur.left:
                        lefts.appendleft(cur.left)
                    if cur.right:
                        rights.appendleft(cur.right)
                        
        return ans
