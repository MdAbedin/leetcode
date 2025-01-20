class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        R,C,n = len(mat),len(mat[0]),len(arr)
        coords = {mat[r][c]:[r,c] for r in range(R) for c in range(C)}
        parents_v = list(range(n+1))
        parents_h = list(range(n+1))
        sizes_v = [1]*(n+1)
        sizes_h = [1]*(n+1)

        def union(x1,x2,parents,sizes):
            sizes[find(x2,parents)] += sizes[find(x1,parents)]
            parents[find(x1,parents)] = find(x2,parents)

        def find(x,parents):
            if parents[x] != x: parents[x] = find(parents[x],parents)
            return parents[x]

        for i,x in enumerate(arr):
            r,c = coords[x]
            mat[r][c] *= -1

            if r-1 >= 0 and mat[r-1][c] < 0: union(x,abs(mat[r-1][c]),parents_v,sizes_v)
            if r+1 < R and mat[r+1][c] < 0: union(x,abs(mat[r+1][c]),parents_v,sizes_v)
            if c-1 >= 0 and mat[r][c-1] < 0: union(x,abs(mat[r][c-1]),parents_h,sizes_h)
            if c+1 < C and mat[r][c+1] < 0: union(x,abs(mat[r][c+1]),parents_h,sizes_h)

            if sizes_v[find(x,parents_v)] == R or sizes_h[find(x,parents_h)] == C: return i
