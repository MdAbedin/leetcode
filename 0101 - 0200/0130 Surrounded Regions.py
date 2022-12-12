class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        bfs = deque()
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if (y == 0 or y == len(board)-1 or x == 0 or x == len(board[0])-1) and board[y][x]=='O':
                    board[y][x] = 'M'
                    bfs.append([y,x])
                    
        while bfs:
            y,x = bfs.popleft()
            
            for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                ny, nx = y+dy, x+dx
                
                if ny >= 0 and ny < len(board) and nx >= 0 and nx < len(board[0]) and board[ny][nx] == 'O':
                    board[ny][nx] = 'M'
                    bfs.append([ny,nx])
                    
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'O': board[y][x] = 'X'
                if board[y][x] == 'M': board[y][x] = 'O'
