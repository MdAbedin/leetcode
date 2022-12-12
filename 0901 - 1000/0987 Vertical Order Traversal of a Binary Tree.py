# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        min_x, max_x = 0, 0
        bfs = deque([[root, 0]])
        
        while bfs:
            cur, cx = bfs.popleft()
            min_x, max_x = min(min_x, cx), max(max_x, cx)
            if cur.left: bfs.append([cur.left, cx-1])
            if cur.right: bfs.append([cur.right, cx+1])
        
        reports = [[] for _ in range(max_x-min_x+1)]
        bfs = deque([[root, 0, 0]])
        
        while bfs:
            new_reports = [[] for _ in range(len(reports))]
            
            for i in range(len(bfs)):
                cur, cx, cy = bfs.popleft()
                new_reports[cx-min_x].append(cur.val)

                if cur.left: bfs.append([cur.left, cx-1, cy-1])
                if cur.right: bfs.append([cur.right, cx+1, cy-1])
            
            for i in range(len(reports)):
                reports[i] += sorted(new_reports[i])
                
        return reports
