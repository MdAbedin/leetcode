class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        seen = {tuple(map(tuple, board))}
        bfs = deque([[board, 0]])
        
        while bfs:
            board, lvl = bfs.popleft()
            if board == [[1,2,3], [4,5,0]]: return lvl
            
            zy = 0 if 0 in board[0] else 1
            zx = board[zy].index(0)
            
            for ny,nx in [[zy+1,zx],[zy-1,zx],[zy,zx+1],[zy,zx-1]]:
                if 0<=ny<2 and 0<=nx<3:
                    new_board = deepcopy(board)
                    
                    new_board[zy][zx] = new_board[ny][nx]
                    new_board[ny][nx] = 0
                    new_tuple = tuple(map(tuple, new_board))
                    
                    if new_tuple not in seen:
                        seen.add(new_tuple)
                        bfs.append([new_board, lvl+1])
            
        return -1
