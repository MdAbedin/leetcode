class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs = deque([root])
        level = 0

        while bfs:
            vals = [node.val for node in bfs]

            if level%2 == 0 and (any(val%2 == 0 for val in vals) or any(v2 <= v1 for v1,v2 in pairwise(vals))): return False
            if level%2 == 1 and (any(val%2 == 1 for val in vals) or any(v2 >= v1 for v1,v2 in pairwise(vals))): return False

            for i in range(len(bfs)):
                node = bfs.popleft()

                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)

            level += 1

        return True
