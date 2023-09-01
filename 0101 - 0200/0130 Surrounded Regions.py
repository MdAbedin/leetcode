class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R,C = len(board),len(board[0])
        edge_region_o_coords = set()

        for r in range(R):
            for c in range(C):
                if not(r in [0,R-1] or c in [0,C-1]) or board[r][c] == "X" or (r,c) in edge_region_o_coords: continue

                edge_region_o_coords.add((r,c))
                dfs = [(r,c)]

                while dfs:
                    cr,cc = dfs.pop()

                    for r2,c2 in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                        if r2 not in range(R) or c2 not in range(C) or board[r2][c2] != "O" or (r2,c2) in edge_region_o_coords: continue
                        edge_region_o_coords.add((r2,c2))
                        dfs.append((r2,c2))

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O" and (r,c) not in edge_region_o_coords: board[r][c] = "X"
