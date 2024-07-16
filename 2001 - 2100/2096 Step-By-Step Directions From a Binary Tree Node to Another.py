class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        g = defaultdict(list)
        bfs = [root]
        start = None

        for node in bfs:
            if node.val == startValue: start = node

            for node2,d in [[node.left,"L"],[node.right,"R"]]:
                if not node2: continue
                g[node].append([node2,d])
                g[node2].append([node,"U"])
                bfs.append(node2)

        bfs = [start]
        seen = {start}
        moves = {}

        for node in bfs:
            if node.val == destValue:
                ans = []

                while node in moves:
                    node,move = moves[node]
                    ans.append(move)

                return "".join(ans[::-1])

            for node2,d in g[node]:
                if not node2 or node2 in seen: continue
                seen.add(node2)
                bfs.append(node2)
                moves[node2] = [node,d]
