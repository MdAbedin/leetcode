class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        nbs = defaultdict(list)
        
        for a,b in edges:
            nbs[a].append(b)
            nbs[b].append(a)
            
        dfs = [[0,0,1]]
        subtree_sizes = defaultdict(int)
        parents = defaultdict(lambda: -1)
        ans_0 = 0
        
        while dfs:
            n,l,c = dfs[-1]            
            
            if c == 1:
                ans_0 += l
                dfs[-1][2] += 1
                for nb in nbs[n]:
                    if nb != parents[n]:
                        dfs.append([nb,l+1,1])
                        parents[nb] = n
            else:
                dfs.pop()
                for nb in nbs[n]:
                    subtree_sizes[n] += subtree_sizes[nb]
                subtree_sizes[n] += 1
                    
        ans = [0]*N
        ans[0] = ans_0
        bfs = deque(nbs[0])
        
        while bfs:
            n = bfs.popleft()
            p = parents[n]
            
            ans[n] = ans[p] + (N-subtree_sizes[n]-1) - (subtree_sizes[n]-1)
            
            for nb in nbs[n]:
                if nb != parents[n]:
                    bfs.append(nb)
        
        return ans
