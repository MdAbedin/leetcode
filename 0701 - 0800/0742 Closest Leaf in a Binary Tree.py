# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        neighbors = defaultdict(list)
        dfs = [root]
        k_node = None
        while dfs:
            node = dfs.pop()
            if node.val == k: k_node = node

            for child in [node.left,node.right]:
                if child:
                    neighbors[node].append(child)
                    neighbors[child].append(node)
                    dfs.append(child)

        bfs = deque([k_node])
        seen = {k_node}
        while bfs:
            node = bfs.popleft()
            if not node.left and not node.right: return node.val

            for nei in neighbors[node]:
                if nei not in seen:
                    seen.add(nei)
                    bfs.append(nei)
