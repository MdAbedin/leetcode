class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        g = defaultdict(list)
        for i,f in enumerate(favorite): g[f].append(i)

        ans = 0
        seen = set()

        for i,f in enumerate(favorite):
            if favorite[f] != i or i in seen: continue

            for v0 in [i,f]:
                bfs = [[v0,0]]
                seen.add(v0)

                for v,d in bfs:
                    for v2 in g[v]:
                        if v2 in seen or v2 in [i,f]: continue
                        seen.add(v2)
                        bfs.append([v2,d+1])

                ans += 1+bfs[-1][1]

        for i in range(len(favorite)):
            if i in seen: continue

            path = [i]
            seen.add(i)
            
            while favorite[path[-1]] not in seen:
                seen.add(favorite[path[-1]])
                path.append(favorite[path[-1]])

            if favorite[path[-1]] in path: ans = max(ans,len(path)-path.index(favorite[path[-1]]))

        return ans
