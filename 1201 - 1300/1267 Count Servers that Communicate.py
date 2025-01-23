class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        r_counts,c_counts = Counter(r for r,c in product(range(R),range(C)) if grid[r][c]),Counter(c for r,c in product(range(R),range(C)) if grid[r][c])
        return sum(map(sum,grid))-sum(r_counts[r] == c_counts[c] == 1 for r,c in product(range(R),range(C)) if grid[r][c])
