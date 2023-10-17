class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        roots = set(range(n))
        g = defaultdict(list)

        for i,neis in enumerate(zip(leftChild,rightChild)):
            for nei in neis:
                roots.discard(nei)
                if nei != -1: g[i].append(nei)

        if len(roots) != 1: return False
        
        root = next(iter(roots))
        dfs = [root]
        seen = {root}

        while dfs:
            v = dfs.pop()

            for nei in g[v]:
                if nei in seen: return False
                seen.add(nei)
                dfs.append(nei)

        return len(seen) == n
