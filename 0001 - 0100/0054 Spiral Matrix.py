class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R,C = len(matrix),len(matrix[0])
        r0,r1,c0,c1 = 0,R-1,0,C-1
        r,c = 0,0
        dr,dc = 0,1
        ans = []

        while len(ans) < R*C:
            ans.append(matrix[r][c])
            
            if r+dr not in range(r0,r1+1) or c+dc not in range(c0,c1+1):
                if dc == 1: r0 += 1
                if dc == -1: r1 -= 1
                if dr == 1: c1 -= 1
                if dr == -1: c0 += 1
                dr,dc = dc,-dr
            
            r += dr
            c += dc

        return ans
