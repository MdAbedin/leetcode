class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R,C = len(matrix),len(matrix[0])
        v_streaks = [[0]*C for i in range(R)]
        h_streaks = [[0]*C for i in range(R)]

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == "1":
                    v_streaks[r][c] = 1 + (v_streaks[r-1][c] if r-1 >= 0 else 0)
                    h_streaks[r][c] = 1 + (h_streaks[r][c-1] if c-1 >= 0 else 0)

        ans = 0

        for r in range(R):
            for c in range(C):
                h = inf

                for c2 in range(c,-1,-1):
                    h = min(h,v_streaks[r][c2])
                    ans = max(ans,h*(c-c2+1))

                w = inf

                for r2 in range(r,-1,-1):
                    w = min(w,h_streaks[r2][c])
                    ans = max(ans,w*(r-r2+1))

        return ans
