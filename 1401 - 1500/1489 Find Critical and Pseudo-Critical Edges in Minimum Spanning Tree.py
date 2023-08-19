class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted([[v1,v2,w,i] for i,(v1,v2,w) in enumerate(edges)],key = lambda edge: edge[2])

        def find(v,parents):
            if parents[v] != v: parents[v] = find(parents[v],parents)
            return parents[v]

        def union(v1,v2,parents):
            parents[find(v1,parents)] = find(v2,parents)

        def get_mst_weight(included_edge_sorted_index, excluded_edge_sorted_index):
            parents = list(range(n))
            mst_weight = 0

            if included_edge_sorted_index != None:
                union(edges[included_edge_sorted_index][0],edges[included_edge_sorted_index][1],parents)
                mst_weight += edges[included_edge_sorted_index][2]

            for sorted_i,(v1,v2,w,original_i) in enumerate(edges):
                if find(v1,parents) == find(v2,parents) or sorted_i == excluded_edge_sorted_index: continue
                
                union(v1,v2,parents)
                mst_weight += w

            return mst_weight

        mst_weight = get_mst_weight(None,None)
        ans = [[],[]]

        for sorted_i,(v1,v2,w,original_i) in enumerate(edges):
            if get_mst_weight(sorted_i,None) != mst_weight: continue

            if get_mst_weight(None,sorted_i) != mst_weight: ans[0].append(original_i)
            else: ans[1].append(original_i)

        return ans
