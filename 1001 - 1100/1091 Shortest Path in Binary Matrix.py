class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1

        N = len(grid)
        bfs = deque([[0,0]])
        seen = {(0,0)}
        length = 1

        while bfs:
            for i in range(len(bfs)):
                r,c = bfs.popleft()
                if [r,c] == [N-1,N-1]: return length

                for dr,dc in product([-1,0,1],repeat=2):
                    r2,c2 = r+dr,c+dc

                    if r2 in range(N) and c2 in range(N) and grid[r2][c2] == 0 and (r2,c2) not in seen:
                        seen.add((r2,c2))
                        bfs.append([r2,c2])

            length += 1

        return -1
