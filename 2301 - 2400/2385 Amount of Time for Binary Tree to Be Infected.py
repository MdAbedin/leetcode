class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        bfs = [root]

        for node in bfs:
            if node.val == start: start_node = node

            for child in [node.left,node.right]:
                if not child: continue

                g[node].append(child)
                g[child].append(node)
                bfs.append(child)

        bfs = [(start_node,0)]
        seen = {start_node}

        for node,t in bfs:
            ans = t

            for nei in g[node]:
                if nei in seen: continue

                seen.add(nei)
                bfs.append((nei,t+1))

        return ans
