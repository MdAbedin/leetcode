class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r0,r1,c0,c1 = 0,n-1,0,n-1
        r,c = 0,0
        dr,dc = 0,1
        ans = [[None]*n for i in range(n)]

        for i in range(n**2):
            ans[r][c] = i+1
            
            if r+dr not in range(r0,r1+1) or c+dc not in range(c0,c1+1):
                if dc == 1: r0 += 1
                if dc == -1: r1 -= 1
                if dr == 1: c1 -= 1
                if dr == -1: c0 += 1
                dr,dc = dc,-dr
            
            r += dr
            c += dc

        return ans
