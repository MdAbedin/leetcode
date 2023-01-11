class TicTacToe:

    def __init__(self, n: int):
        self.board = [[None]*n for i in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if any(row == [player]*len(row) for row in self.board): return player
        if any(col == [player]*len(col) for col in map(list,zip(*self.board))): return player
        if all(self.board[i][i] == player for i in range(len(self.board))): return player
        if all(self.board[i][~i] == player for i in range(len(self.board))): return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
