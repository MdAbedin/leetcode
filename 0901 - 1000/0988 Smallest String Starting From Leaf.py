# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        dfs = [root]
        bfs = deque()
        root.parent = None

        while dfs:
            cur = dfs.pop()

            if not cur.left and not cur.right: bfs.append(cur)

            if cur.left:
                cur.left.parent = cur
                dfs.append(cur.left)
            
            if cur.right:
                cur.right.parent = cur
                dfs.append(cur.right)

        ans = []

        while bfs:
            min_char = min(node.val for node in bfs)
            ans.append(min_char)

            for i in range(len(bfs)):
                cur = bfs.popleft()
                
                if cur.val == min_char:
                    if cur.parent:
                        bfs.append(cur.parent)
                    else:
                        return "".join(chr(ord('a') + val) for val in ans)
