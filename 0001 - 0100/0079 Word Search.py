class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board),len(board[0])

        def works(r,c,i,seen):
            if not(r in range(R) and c in range(C) and board[r][c] == word[i] and (r,c) not in seen): return False
            if i == len(word)-1: return True
            return any(works(r2,c2,i+1,seen|{(r,c)}) for r2,c2 in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)))

        return all(any(c in row for row in board) for c in word) and any(works(r,c,0,set()) for r in range(R) for c in range(C))
