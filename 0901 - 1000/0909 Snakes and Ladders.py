class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        bfs = deque([(N-1,0)])
        seen = {(N-1,0)}
        moves = 0
        
        while bfs:
            for i in range(len(bfs)):
                r,c = bfs.popleft()
                dc = 1 if (N-1-r)%2 == 0 else -1
                
                if r == 0 and c+dc not in range(N): return moves
                
                for move in range(6):
                    if c+dc not in range(N):
                        r -= 1
                        dc *= -1
                    else:
                        c += dc
                        
                    if r == -1: break
                        
                    if board[r][c] == -1:
                        r2,c2 = r,c
                    else:
                        r2 = N-1 - ((board[r][c]-1) // N)
                        c2 = (board[r][c]-1)%N if (N-1-r2)%2 == 0 else N-1-(board[r][c]-1)%N
                    
                    if (r2,c2) not in seen:
                        seen.add((r2,c2))
                        bfs.append((r2,c2))
                    
            moves += 1
        
        return -1
