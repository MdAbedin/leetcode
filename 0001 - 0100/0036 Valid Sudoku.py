class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(values):
            filled_values = list(filter(partial(ne, "."), values))
            return len(filled_values) == len(set(filled_values))

        rows_valid = all(map(is_valid, board))
        cols_valid = all(map(is_valid, zip(*board)))
        blocks_valid = all(is_valid([board[r][c] for r in range(i//3*3,i//3*3+3) for c in range(i%3*3,i%3*3+3)]) for i in range(9))

        return rows_valid and cols_valid and blocks_valid
