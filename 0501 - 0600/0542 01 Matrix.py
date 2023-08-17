class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R,C = len(mat),len(mat[0])
        bfs = deque((r,c) for r in range(R) for c in range(C) if mat[r][c] == 0)
        seen = set(bfs)
        ans = [[None]*C for r in range(R)]
        d = 0

        while bfs:
            for i in range(len(bfs)):
                r,c = bfs.popleft()
                ans[r][c] = d

                for r2,c2 in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if r2 in range(R) and c2 in range(C) and (r2,c2) not in seen:
                        seen.add((r2,c2))
                        bfs.append((r2,c2))

            d += 1            

        return ans
