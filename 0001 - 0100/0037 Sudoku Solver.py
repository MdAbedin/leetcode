class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def solve(r,c):
            if c == 9: return r == 8 or solve(r+1,0)
            if board[r][c] != ".": return solve(r,c+1)

            possible_digits = set(digits[1:]) - set(board[r]) - set(next(islice(zip(*board),c,None))) - {board[r2][c2] for r2 in range(9) for c2 in range(9) if [r2//3,c2//3] == [r//3,c//3]}

            for digit in possible_digits:
                board[r][c] = digit
                if solve(r,c+1): return True
                board[r][c] = "."

            return False

        solve(0,0)
