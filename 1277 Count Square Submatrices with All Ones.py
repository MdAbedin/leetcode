class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 1:
                    y_streak = matrix[y-1][x][0]+1 if y-1>=0 else 1
                    x_streak = matrix[y][x-1][1]+1 if x-1>= 0 else 1
                    square_streak = min(matrix[y-1][x-1][2]+1 if (y-1>=0 and x-1>= 0) else 1, y_streak, x_streak)
                    matrix[y][x] = [y_streak, x_streak, square_streak]
                    ans += square_streak
                else:
                    matrix[y][x] = [0,0,0]
                    
        return ans
