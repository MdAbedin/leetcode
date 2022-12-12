# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        bfs = deque([root])
        parents = {root: None}
        
        while bfs:
            for node in bfs:
                if node.right in parents:
                    if parents[node].left == node: parents[node].left = None
                    if parents[node].right == node: parents[node].right = None
                    return root
                
            new_parents = dict()
            
            for i in range(len(bfs)):
                cur = bfs.popleft()
                if cur.left:
                    new_parents[cur.left] = cur
                    bfs.append(cur.left)
                if cur.right:
                    new_parents[cur.right] = cur
                    bfs.append(cur.right)
                    
            parents = new_parents
