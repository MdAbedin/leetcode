class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for y in range(len(board)):
            for x in range(len(board[0])):
                living_neighbors = 0
                
                for y2, x2 in starmap(lambda dy,dx: (y+dy, x+dx), product((0,-1,+1), (0,-1,+1))):
                    if [y2,x2] != [y,x] and y2 >= 0 and x2 >= 0 and y2 < len(board) and x2 < len(board[0]):
                        if board[y2][x2] in [1,2]:
                            living_neighbors += 1
                            
                if board[y][x]:
                    if not living_neighbors in [2,3]:
                        board[y][x] = 2
                else:
                    if living_neighbors == 3:
                        board[y][x] = 3
                        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] >= 2:
                    board[y][x] -= 2
