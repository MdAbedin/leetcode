class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        neighbors = defaultdict(list)
        dfs = [root]

        while dfs:
            node = dfs.pop()

            if node.left:
                dfs.append(node.left)
                neighbors[node].append(node.left)
                neighbors[node.left].append(node)
                
            if node.right:
                dfs.append(node.right)
                neighbors[node].append(node.right)
                neighbors[node.right].append(node)

        bfs = deque([target])
        seen = {target}

        for i in range(k):
            for i2 in range(len(bfs)):
                node = bfs.popleft()

                for nei in neighbors[node]:
                    if nei not in seen:
                        seen.add(nei)
                        bfs.append(nei)

        return [node.val for node in bfs]
