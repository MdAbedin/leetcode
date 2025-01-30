class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        ans = defaultdict(lambda:-1)

        for v1,v2 in edges:
            g[v1].add(v2)
            g[v2].add(v1)

        for v0 in range(1,n+1):
            bfs = {v0}
            seen = {v0}
            ans2 = 0

            while bfs:
                ans2 += 1
                bfs2 = {v2 for v in bfs for v2 in g[v] if v2 not in seen}
                seen |= bfs2
                if ans2 == 1 and any(v2 in bfs2 for v in bfs2 for v2 in g[v]): break

                for v in bfs2.copy():
                    if not g[v]&bfs2 or g[v]-seen: continue
                    bfs2.remove(v)

                if any(v2 in bfs2 for v in bfs2 for v2 in g[v]): break
                bfs = bfs2
            else: ans[m] = max(ans[m:=min(seen)],ans2)
            if (m:=min(seen)) not in ans: ans[m] = -1

        return -1 if -1 in ans.values() else sum(ans.values())
